import type { Chapter, Explanation, LeaderboardData } from "@/types";
import { defineStore } from "pinia";
import { computed, reactive, ref } from "vue";
import { smartParse, smartToString, slugifyDot } from "@/utils/stringify.ts";
import { preloadImage, preloadImages } from "@/utils/image.ts";
import { apiUrl } from "@/utils/api.ts";

type AnswerData = {
  answerIndex: number;
  correct: boolean;
  answerText?: string;
};

type FinishedChapterData = {
  score: number;
  answers: Map<number, AnswerData>;
};

function postJson(url: string, payload: object) {
  return fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
}

export const useStore = defineStore("store", () => {
  const homeDataLoaded = ref(false);
  const chapterDataLoaded = reactive(new Map<number, boolean>());

  // user guid (does not change after reset)
  const userGUID = ref("");
  // attempt guid (does change after reset)
  const attemptGUID = ref("");
  const attemptStreak = ref(0);
  const consentClickedButNotDone = ref(false);
  const hasConsented = ref(false);
  const ensuredFinishedChaptersSent = ref(false);

  // temp array of requests before consent is given
  const preConsentRequests = ref<Array<{ url: string; payload: object }>>([]);

  // intro texts
  const introductionTitle = ref("");
  const introductionDescription = ref("");
  const introductionButtonText = ref("");
  const introductionButtonTextSecondary = ref("");

  // chapters
  const chapters = reactive(new Map<number, Chapter>());
  const explanations = reactive(new Map<number, Explanation>());

  // ids of just unlocked chapters
  const justUnlockedChapters = ref<number[]>([]);
  // ids of all unlocked chapters
  const unlockedChapters = ref<number[]>([]);
  // ids of finished chapters to score and answers
  const finishedChapters = reactive(new Map<number, FinishedChapterData>());
  // ids of in progress chapters to score and answers
  const inProgressChapters = reactive(new Map<number, FinishedChapterData>());

  // user answers
  const currentChapterId = ref(-1);
  const currentChapterScore = ref(0);
  // ids of pages to answers
  const currentChapterAnswers = reactive(new Map<number, AnswerData>());

  function setCurrentChapter(id: number) {
    currentChapterId.value = id;
    if (finishedChapters.has(id)) {
      const data = finishedChapters.get(id);
      if (data) {
        currentChapterScore.value = data.score;
        currentChapterAnswers.clear();
        for (const [k, v] of data.answers.entries()) {
          currentChapterAnswers.set(k, v);
        }
      } else {
        currentChapterScore.value = 0;
        currentChapterAnswers.clear();
      }
    } else if (inProgressChapters.has(id)) {
      const data = inProgressChapters.get(id);
      if (data) {
        currentChapterScore.value = data.score;
        currentChapterAnswers.clear();
        for (const [k, v] of data.answers.entries()) {
          currentChapterAnswers.set(k, v);
        }
      } else {
        currentChapterScore.value = 0;
        currentChapterAnswers.clear();
      }
    } else {
      currentChapterScore.value = 0;
      currentChapterAnswers.clear();
    }
  }

  function clearCurrentChapter() {
    setCurrentChapter(-1);
  }

  async function giveConsent() {
    if (hasConsented.value || consentClickedButNotDone.value) {
      return;
    }

    consentClickedButNotDone.value = true;
    // send all pre consent data to backend
    for (const req of preConsentRequests.value) {
      const res = await postJson(req.url, req.payload);
      // eslint-disable-next-line no-console
      console.log("Pre consent request sent", req.url, res.status);
    }

    preConsentRequests.value = [];
    consentClickedButNotDone.value = false;
    hasConsented.value = true;
    saveLocalStorage();
  }

  function generateGUID() {
    const one = Math.random().toString(36).substring(2);
    const two = Math.random().toString(36).substring(2);
    return one + two;
  }

  function clearAllProgress() {
    attemptGUID.value = generateGUID();
    attemptStreak.value = 0;
    hasConsented.value = false;
    ensuredFinishedChaptersSent.value = false;
    preConsentRequests.value = [];
    justUnlockedChapters.value = [];
    unlockedChapters.value = [];
    finishedChapters.clear();
    inProgressChapters.clear();
    clearCurrentChapter();
    clearLocalStorage();
  }

  function clearLocalStorage() {
    const s = window.localStorage;
    s.setItem("attemptGUID", attemptGUID.value);
    s.removeItem("attemptStreak");
    s.removeItem("hasConsented");
    s.removeItem("ensuredFinishedChaptersSent");
    s.removeItem("preConsentRequests");
    s.removeItem("justUnlockedChapters");
    s.removeItem("unlockedChapters");
    s.removeItem("finishedChapters");
    s.removeItem("inProgressChapters");
  }

  function saveLocalStorage() {
    const s = window.localStorage;
    s.setItem("userGUID", userGUID.value);
    s.setItem("attemptGUID", attemptGUID.value);
    s.setItem("attemptStreak", attemptStreak.value.toString());
    s.setItem("hasConsented", hasConsented.value.toString());
    s.setItem(
      "ensuredFinishedChaptersSent",
      ensuredFinishedChaptersSent.value.toString(),
    );
    s.setItem("preConsentRequests", smartToString(preConsentRequests));
    s.setItem("justUnlockedChapters", smartToString(justUnlockedChapters));
    s.setItem("unlockedChapters", smartToString(unlockedChapters));
    s.setItem("finishedChapters", smartToString(finishedChapters));
    s.setItem("inProgressChapters", smartToString(inProgressChapters));
  }

  function loadLocalStorage() {
    const s = window.localStorage;
    let item: string | null = null;

    // load user guid
    if ((item = s.getItem("userGUID"))) {
      userGUID.value = item;
    } else {
      userGUID.value = generateGUID();
      s.setItem("userGUID", userGUID.value);
    }

    // load attempt guid
    if ((item = s.getItem("attemptGUID"))) {
      attemptGUID.value = item;
    } else {
      attemptGUID.value = generateGUID();
      s.setItem("attemptGUID", attemptGUID.value);
    }

    // load attempt streak
    if ((item = s.getItem("attemptStreak"))) {
      const value = Number.parseInt(item, 10);
      if (!Number.isNaN(value) && value >= 0) {
        attemptStreak.value = value;
      }
    }

    // load consent
    if ((item = s.getItem("hasConsented"))) {
      hasConsented.value = item === "true";
    }

    // load ensured finished chapters sent
    if ((item = s.getItem("ensuredFinishedChaptersSent"))) {
      ensuredFinishedChaptersSent.value = item === "true";
    }

    // load pre consent requests
    if ((item = s.getItem("preConsentRequests"))) {
      const value = smartParse(item) as Array<{ url: string; payload: object }>;
      preConsentRequests.value = value;
    }

    // load saved data
    if ((item = s.getItem("justUnlockedChapters"))) {
      const value = smartParse(item) as number[];
      justUnlockedChapters.value = value;
    }
    if ((item = s.getItem("unlockedChapters"))) {
      const value = smartParse(item) as number[];
      unlockedChapters.value = value;
    }
    if ((item = s.getItem("finishedChapters"))) {
      const value = smartParse(item) as Map<number, FinishedChapterData>;
      finishedChapters.clear();
      for (const [k, v] of value.entries()) {
        finishedChapters.set(k, v);
      }
    }
    if ((item = s.getItem("inProgressChapters"))) {
      const value = smartParse(item) as Map<number, FinishedChapterData>;
      inProgressChapters.clear();
      for (const [k, v] of value.entries()) {
        inProgressChapters.set(k, v);
      }
    }
  }

  // total score
  const score = computed(() => {
    return [...finishedChapters.values()].reduce(
      (prev, curr) => prev + curr.score,
      0,
    );
  });

  async function fetchHomeData() {
    const response = await fetch(`${apiUrl}/api/home/`);

    if (response.status === 200) {
      const data = await response.json();
      introductionTitle.value = data.title;
      introductionDescription.value = data.description;
      preloadImages(data.description_images);
      introductionButtonText.value = data.button_text;
      introductionButtonTextSecondary.value = data.button_text_secondary;

      chapters.clear();
      for (const c of data.chapters) {
        chapters.set(c.id, c);
        if (c.image) {
          preloadImage(c.image);
        }
      }

      explanations.clear();
      for (const e of data.explanations) {
        explanations.set(e.id, e);
      }

      homeDataLoaded.value = true;
    }
  }

  async function initHomeData() {
    if (!homeDataLoaded.value) {
      await fetchHomeData();
    }
  }

  function getChapterIdBySlug(slug: string) {
    for (const chapter of chapters.values()) {
      if (slugifyDot(chapter.title) === slug) {
        return chapter.id;
      }
    }
    return -1;
  }

  async function fetchChapterData(id: number) {
    const response = await fetch(`${apiUrl}/api/chapter/${id}/`);

    if (response.status === 200) {
      const data = await response.json();
      const chapter = chapters.get(id);
      if (chapter) {
        chapter.pages = data.pages;

        chapterDataLoaded.set(chapter.id, true);
      }
    }
  }

  async function initChapterData(id: number) {
    if (!chapterDataLoaded.get(id)) {
      await fetchChapterData(id);
    }
  }

  async function wrapConsentPost(url: string, payload: object) {
    if (!hasConsented.value) {
      // eslint-disable-next-line no-console
      console.log("No consent, not sending data to API");
      preConsentRequests.value.push({ url, payload });
      return {
        status: -1,
        json: async () => null,
      };
    }
    return postJson(url, payload);
  }

  async function sendChapterDataToApi(
    data: FinishedChapterData | undefined,
    url: string,
  ) {
    if (data) {
      try {
        const response = await wrapConsentPost(url, {
          userGUID: userGUID.value,
          attemptGUID: attemptGUID.value,
          data: smartToString(data),
        });
        if (response.status === 200) {
          const data = await response.json();
          // eslint-disable-next-line no-console
          console.log("sendChapterDataToApi", data);
        }
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error("sendChapterDataToApi", error);
      }
    } else {
      // eslint-disable-next-line no-console
      console.error("sendChapterDataToApi", "no data");
    }
  }

  async function sendFinishedChapterDataToApi(chapterId: number) {
    const data = finishedChapters.get(chapterId);
    return sendChapterDataToApi(
      data,
      `${apiUrl}/api/chapter/${chapterId}/finished/`,
    );
  }

  async function sendProgressChapterDataToApi(chapterId: number) {
    const data = inProgressChapters.get(chapterId);
    return sendChapterDataToApi(
      data,
      `${apiUrl}/api/chapter/${chapterId}/progress/`,
    );
  }

  async function ensureFinishedChaptersSent() {
    if (!hasConsented.value) {
      // eslint-disable-next-line no-console
      console.log("No consent, not sending data to API");
      return;
    }
    if (ensuredFinishedChaptersSent.value) {
      // eslint-disable-next-line no-console
      console.log(
        "ensureFinishedChaptersSent not called, this is a one time fix",
      );
      return;
    }
    // eslint-disable-next-line no-console
    console.log("ensureFinishedChaptersSent called");
    const dataToSend = [];
    for (const chapterId of finishedChapters.keys()) {
      const chapterData = finishedChapters.get(chapterId);
      if (chapterData && chapterData.score) {
        // eslint-disable-next-line no-console
        console.log("Chapter data", chapterId, chapterData.score);
        dataToSend.push({ id: chapterId, score: chapterData.score });
      }
    }
    try {
      if (dataToSend.length != 0) {
        const response = await postJson(
          `${apiUrl}/api/ensure-finished-chapter-scores/`,
          {
            userGUID: userGUID.value,
            attemptGUID: attemptGUID.value,
            data: smartToString(dataToSend),
          },
        );
        if (response.status === 200) {
          const data = await response.json();
          // eslint-disable-next-line no-console
          console.log("ensureFinishedChaptersSent", data);
          ensuredFinishedChaptersSent.value = true;
          saveLocalStorage();
        }
      }
    } catch (error) {
      // eslint-disable-next-line no-console
      console.error("ensureFinishedChaptersSent", error);
    }
  }

  async function fetchPageCorrectPercent(chapterId: number, pageId: number) {
    try {
      const response = await fetch(
        `${apiUrl}/api/chapter/${chapterId}/page/${pageId}/stats/`,
      );
      if (response.status === 200) {
        const data = await response.json();
        return data.percent_correct;
      }
    } catch (error) {
      // eslint-disable-next-line no-console
      console.error("fetchPageCorrectPercent", error);
    }
    return null;
  }

  async function fetchLeaderboard(): Promise<LeaderboardData | null> {
    if (!hasConsented.value) {
      return null;
    }
    try {
      const response = await fetch(
        `${apiUrl}/api/leaderboard/?attempt_guid=${attemptGUID.value}`,
      );
      if (response.status === 200) {
        const data = await response.json();
        return data;
      }
    } catch (error) {
      // eslint-disable-next-line no-console
      console.error("fetchLeaderboard", error);
    }
    return null;
  }

  async function submitLeaderboardNickname(nickname: string): Promise<boolean> {
    if (!hasConsented.value) {
      return false;
    }
    try {
      const response = await postJson(`${apiUrl}/api/leaderboard/nickname/`, {
        userGUID: userGUID.value,
        attemptGUID: attemptGUID.value,
        nickname,
      });
      if (response.status === 200) {
        return true;
      }
    } catch (error) {
      // eslint-disable-next-line no-console
      console.error("submitLeaderboardNickname", error);
    }
    return false;
  }

  return {
    initHomeData,
    homeDataLoaded,
    getChapterIdBySlug,
    initChapterData,
    chapterDataLoaded,
    //
    userGUID,
    attemptGUID,
    introductionTitle,
    introductionDescription,
    introductionButtonText,
    introductionButtonTextSecondary,
    chapters,
    explanations,
    justUnlockedChapters,
    unlockedChapters,
    finishedChapters,
    inProgressChapters,
    currentChapterId,
    currentChapterScore,
    currentChapterAnswers,
    attemptStreak,
    hasConsented,
    consentClickedButNotDone,
    giveConsent,
    setCurrentChapter,
    clearCurrentChapter,
    clearAllProgress,
    saveLocalStorage,
    loadLocalStorage,
    score,
    sendFinishedChapterDataToApi,
    sendProgressChapterDataToApi,
    ensureFinishedChaptersSent,
    fetchPageCorrectPercent,
    fetchLeaderboard,
    submitLeaderboardNickname,
  };
});
