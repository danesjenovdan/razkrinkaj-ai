<script setup lang="ts">
import { ref } from "vue";

const newsletterEmail = ref("");
const newsletterConsent = ref(false);
const newsletterLoading = ref(false);

async function onNewsletterSubmit() {
  const email = newsletterEmail.value;

  const campaign_slug = "danes-je-nov-dan";
  const segment_id = 21;

  let url = `https://moj.djnd.si/${campaign_slug}/prijava?segment_id=${segment_id}`;
  url += `&email=${encodeURIComponent(email)}`;
  window.open(`${url}`, `_blank`);
}
</script>

<template>
  <footer>
    <div class="page-gutter bg-kvizle-color-3">
      <div class="page-footer">
        <div class="footer-col about-section">
          <div class="footer-block">
            Za <strong>volilni Kvizle</strong> skrbi<br />
            <a
              href="https://danesjenovdan.si"
              target="_blank"
              rel="noopener noreferrer"
              >Danes je nov dan, Inštitut za druga vprašanja</a
            >
          </div>
          <div class="footer-block">
            <a
              href="https://danesjenovdan.si/politika-zasebnosti-in-varstva-osebnih-podatkov/"
              target="_blank"
              >Politika zasebnosti in varstva osebnih podatkov</a
            >
          </div>
        </div>
        <div class="footer-col donate-section">
          <div class="footer-block">
            <div>
              <div class="text">
                <div class="title">Podpri naše delo!</div>
                <div class="desc">Izberi višino donacije.</div>
              </div>
              <div class="buttons">
                <a
                  href="https://moj.djnd.si/danes-je-nov-dan/doniraj/info?znesek=11"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="button-link donate-link"
                >
                  <span>11&nbsp;€</span>
                </a>
                <a
                  href="https://moj.djnd.si/danes-je-nov-dan/doniraj/info?znesek=24"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="button-link donate-link"
                >
                  <span>24&nbsp;€</span>
                </a>
                <a
                  href="https://moj.djnd.si/danes-je-nov-dan/doniraj"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="button-link donate-link"
                >
                  <span>Poljubno</span>
                </a>
                <a
                  href="https://moj.djnd.si/danes-je-nov-dan/doniraj?mesecna=true"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="button-link donate-link"
                >
                  <span>Mesečno</span>
                </a>
              </div>
            </div>
          </div>
        </div>
        <div class="footer-col newsletter-section">
          <div class="footer-block">
            <strong>Te zanima, kaj delamo? Naroči se na Občasnik!</strong>
            <form class="newsletter-form" @submit.prevent="onNewsletterSubmit">
              <div class="form-group">
                <label>
                  Vpiši svoj e-naslov
                  <input
                    id="newsletter-email"
                    v-model="newsletterEmail"
                    type="email"
                    required
                  />
                </label>
              </div>
              <div class="form-group">
                <div class="checkbox">
                  <input
                    id="newsletter-checkbox"
                    v-model="newsletterConsent"
                    type="checkbox"
                    required
                  />
                  <label for="newsletter-checkbox">
                    <span>
                      Strinjam se, da mi Danes je nov dan po
                      <span class="nobr">e-pošti</span> pošilja Občasnik in
                      druga obvestila.
                    </span>
                  </label>
                </div>
              </div>
              <div class="form-group">
                <button
                  type="submit"
                  class="button-link submit-button"
                  :disabled="newsletterLoading"
                >
                  NAROČI SE
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped lang="scss">
@use "@sass-fairy/string";
@use "@sass-fairy/url";
@use "@/assets/variables" as vars;
@use "@/assets/mixins";

footer {
  margin-top: auto;

  .page-footer {
    display: flex;
    justify-content: center;
    gap: 4rem;
    max-width: min(65rem, 100%);
    margin-inline: auto;
    padding-block: 2.5rem;

    @media (max-width: 992px) {
      flex-wrap: wrap;
      gap: 2rem;
    }

    @media (max-width: 576px) {
      flex-direction: column;
      gap: 1.25rem;
      padding-block: 1.25rem;
    }

    .footer-col {
      flex: 1;
    }

    .footer-block {
      padding-block: 1rem;
      font-size: 1.125rem;

      @media (max-width: 576px) {
        padding-block: 0.75rem;
        font-size: 1rem;
      }

      strong {
        font-weight: 500;
      }

      a {
        display: inline-block;
        font-weight: 500;
        color: inherit;

        @media (hover: hover) {
          &:hover {
            text-decoration: none;
          }
        }

        @include mixins.focus-visible;
      }

      .button-link {
        @include mixins.button-link;
        padding: 0.45em 1.125em 0.4em;
        font-size: 0.875rem;
        font-weight: 600;
      }
    }

    .about-section {
      @media (max-width: 992px) {
        flex-basis: 100%;
        display: flex;
        gap: 2rem;

        .footer-block {
          flex: 1;
        }
      }

      @media (max-width: 576px) {
        flex-direction: column;
        gap: 0;
      }
    }

    .donate-section {
      flex: 0.8;

      @media (max-width: 992px) {
        flex: 1;
      }

      .footer-block {
        .text {
          .title {
            font-size: 1.125rem;
            font-weight: 600;

            @media (max-width: 576px) {
              font-size: 1rem;
            }
          }

          .desc {
            font-size: 1rem;

            @media (max-width: 576px) {
              font-size: 0.875rem;
            }
          }
        }

        .buttons {
          display: grid;
          grid-template-columns: repeat(2, 1fr);
          gap: 0.5rem;
          max-width: 16rem;
          margin-top: 1rem;

          .donate-link {
            margin-left: 0;
          }
        }
      }
    }

    .newsletter-section {
      .footer-block {
        strong {
          display: inline-block;
          max-width: 15rem;
          font-weight: 600;
        }

        .newsletter-form {
          .form-group {
            margin-top: 1rem;

            &:has(.checkbox) {
              margin-top: 0.5rem;
            }

            label {
              display: flex;
              flex-direction: column;
              font-size: 0.875rem;
              line-height: 1.3;

              input {
                margin-top: 0.25rem;
                padding: 0.25em 0.5em;
                background: var(--color-bg-white);
                border: 1px solid var(--color-text);
                font-weight: 500;
                font-size: 1rem;
                line-height: 1rem;
                color: var(--color-text);

                @include mixins.focus-visible;
              }
            }

            .checkbox {
              display: flex;
              gap: 0.5em;

              input[type="checkbox"] {
                appearance: none;
                display: grid;
                place-items: center;
                margin: 0;
                flex-shrink: 0;
                width: 1.5rem;
                height: 1.5rem;
                background: var(--color-bg-white);
                border: 1px solid var(--color-text);
                color: var(--color-text);

                &:checked {
                  &::before {
                    content: "";
                    display: block;
                    width: 0.4em;
                    height: 0.8em;
                    margin-top: -0.2em;
                    border: 0 solid currentColor;
                    border-width: 0 1px 1px 0;
                    transform-origin: center;
                    transform: rotate(45deg);
                  }
                }

                @include mixins.focus-visible;
              }
            }

            .submit-button {
              min-width: 7.75rem;

              &:disabled {
                cursor: wait;
                filter: grayscale(1);
              }
            }
          }
        }
      }
    }
  }
}
</style>
