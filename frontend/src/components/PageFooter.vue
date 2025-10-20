<script setup lang="ts">
import axios from 'axios'
import { ref } from 'vue'
import MkLogo from './logos/MkLogo.vue'

const newsletterEmail = ref('')
const newsletterConsent = ref(false)
const newsletterLoading = ref(false)

async function onNewsletterSubmit() {
  newsletterLoading.value = true
  try {
    const response = await axios.post(
      'https://podpri.lb.djnd.si/api/subscribe/',
      {
        email: newsletterEmail.value,
        segment_id: 21,
      },
    )
    if (response.data.msg === 'mail sent') {
      newsletterEmail.value = ''
      newsletterConsent.value = false
      newsletterLoading.value = false
      alert(
        'Hvala! Poslali smo ti sporočilo s povezavo, na kateri lahko potrdiš prijavo!',
      )
    } else {
      newsletterLoading.value = false
      alert('Prišlo je do napake :(')
    }
  } catch (error) {
    console.error(error)
    newsletterLoading.value = false
    alert('Prišlo je do napake :(')
  }
}
</script>

<template>
  <footer>
    <div class="page-gutter bg-manipulacija-color-9">
      <div class="page-footer">
        <div class="footer-col">
          <div class="footer-block">
            Za <strong>Manipulacija ni informacija</strong> skrbi<br />
            <a
              href="https://danesjenovdan.si"
              target="_blank"
              rel="noopener noreferrer"
              class="about-link"
              >Danes je nov dan, Inštitut za druga vprašanja</a
            >
          </div>
          <!-- <div class="footer-block">
            <span class="semi-bold">Podpri naše delo.</span>
            <a
              href="https://danesjenovdan.si/podpri-nas/"
              target="_blank"
              rel="noopener noreferrer"
              class="button-link donate-link"
            >
              <span>DONIRAJ</span>
            </a>
          </div> -->
          <div class="footer-block">
            <span class="medium-bold"
              >Preveri tudi naš izobraževalni kviz
            </span>
            <a
              href="https://razkrinkaj.ai/"
              target="_blank"
              rel="noopener noreferrer"
              class="about-link"
              >Razkrinkaj.AI</a
            >
            <span class="medium-bold">
              za prepoznavanje vsebin ustvarjenih z umetno inteligenco!</span
            >
          </div>
        </div>
        <div class="footer-col">
          <div class="footer-block">
            <div class="jagged-box">
              <div class="text">
                <div class="title">Podpri naše delo!</div>
                <div class="desc">Izberi višino donacije.</div>
              </div>
              <div class="buttons">
                <a
                  href="https://moj.djnd.si/danes-je-nov-dan/doniraj/info?znesek=11"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="button-link donate-link larger"
                >
                  <span>11&nbsp;€</span>
                </a>
                <a
                  href="https://moj.djnd.si/danes-je-nov-dan/doniraj/info?znesek=24"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="button-link donate-link larger"
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
        <div class="footer-col">
          <div class="footer-block">
            <span class="semi-bold">
              Te zanima, kaj delamo? Naroči se na Občasnik!
            </span>
            <form class="newsletter-form" @submit.prevent="onNewsletterSubmit">
              <div class="form-group">
                <label>
                  Vpiši svoj e-naslov
                  <input
                    type="email"
                    id="newsletter-email"
                    required
                    v-model="newsletterEmail"
                  />
                </label>
              </div>
              <div class="form-group">
                <div class="checkbox">
                  <input
                    type="checkbox"
                    id="newsletter-checkbox"
                    required
                    v-model="newsletterConsent"
                  />
                  <label for="newsletter-checkbox">
                    <span>
                      Strinjam se, da mi Danes je nov dan po e-pošti pošilja
                      Občasnik in druga obvestila.
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
    <div class="page-gutter bg-white">
      <div class="page-footer page-footer-bottom">
        <div class="footer-col">
          <a
            href="https://danesjenovdan.si/politika-zasebnosti-in-varstva-osebnih-podatkov/"
            target="_blank"
            >Politika zasebnosti in varstva osebnih podatkov</a
          >
        </div>
        <div class="footer-col"></div>
        <div class="footer-col">
          <span>Projekt podpira</span>
          <MkLogo />
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped lang="scss">
@use '@sass-fairy/string';
@use '@sass-fairy/url';
@use '@/assets/variables' as vars;

footer {
  .page-footer {
    display: flex;
    justify-content: center;
    gap: 2rem;
    padding-top: 3.25rem;
    padding-bottom: 2.375rem;

    @media (max-width: 992px) {
      flex-wrap: wrap;
    }

    @media (max-width: 576px) {
      flex-direction: column;
      gap: 1.25rem;
      padding-block: 1.25rem;
    }

    .footer-col {
      flex: 1;
      max-width: 22rem;
      width: min(100%, 24rem);
    }

    .footer-block {
      padding-block: 1.25rem;
      font-size: 1rem;

      strong {
        font-weight: 600;
      }

      .semi-bold {
        font-weight: 600;
      }

      .medium-bold {
        font-weight: 500;
      }

      .about-link {
        font-weight: 600;
        color: inherit;

        &:hover {
          text-decoration: none;
        }
      }

      .jagged-box {
        padding: 1.75rem 2rem;
        background-image: url('/jagged-border-question.svg');
        background-repeat: no-repeat;
        background-size: 100% 100%;

        .text {
          text-align: center;
          text-wrap: pretty;

          .title {
            font-family: var(--font-family-alt);
            font-size: 1.125rem;
            font-weight: 600;
            text-transform: uppercase;
          }

          .desc {
            font-size: 1rem;
            font-weight: 500;
          }
        }

        .buttons {
          display: grid;
          grid-template-columns: 5.375rem 5.375rem;
          justify-content: center;
          gap: 0.5rem;
          margin-top: 1rem;

          .donate-link {
            height: 36px;
            margin-left: 0;
            font-size: 0.875rem;
            line-height: 1.5rem;
            font-weight: 600;
            justify-content: center;

            &.larger {
              font-size: 1.125rem;
            }
          }
        }
      }

      .button-link {
        display: inline-flex;
        gap: 0.5em;
        align-items: center;
        padding: 0.4em 1.125em 0.3em;
        background-color: transparent;
        background-image: url.svg(vars.$button-link-bg-string);
        background-repeat: no-repeat;
        background-size: 100% 100%;
        font-family: var(--font-family-alt);
        font-size: 1.125rem;
        font-weight: 600;
        line-height: 1.3;
        color: inherit;
        text-decoration: none;
        cursor: pointer;
        transition:
          scale 0.15s ease-in-out,
          filter 0.15s ease-in-out;
        will-change: scale, filter;

        &:not(:disabled):hover {
          scale: 1.05;
          filter: drop-shadow(0 0 4px var(--manipulacija-color-4));
        }
      }

      .donate-link {
        $button-link-bg-string-donate: string.replace(
          vars.$button-link-bg-string,
          '#FFF',
          '#{vars.$manipulacija-color-2}'
        );
        background-image: url.svg($button-link-bg-string-donate);
        margin-left: 0.75rem;
      }

      .submit-button {
        $button-link-bg-string-submit: string.replace(
          vars.$button-link-bg-string,
          '#FFF',
          '#{vars.$manipulacija-color-6}'
        );
        background-image: url.svg($button-link-bg-string-submit);
        margin-top: 0.5rem;
        border: 0;

        &:disabled {
          cursor: wait;
          filter: grayscale(1);
        }
      }

      .newsletter-form {
        .form-group {
          margin-top: 0.5rem;

          label {
            display: flex;
            flex-direction: column;
            font-size: 0.75rem;
            line-height: 1.3;

            input {
              margin-top: 0.25rem;
              padding: 0.2em 0.5em;
              background: var(--manipulacija-color-8);
              border: 3px solid #000;
              border-radius: 5px;
              font-weight: 500;
              font-size: 1rem;
              line-height: 1rem;
              color: var(--color-text);
            }
          }

          .checkbox {
            display: flex;
            gap: 0.5em;

            input[type='checkbox'] {
              appearance: none;
              display: grid;
              place-items: center;
              background: var(--manipulacija-color-8);
              margin: 0;
              flex-shrink: 0;
              width: 1.5rem;
              height: 1.5rem;
              border: 3px solid #000;
              border-radius: 5px;
              color: var(--color-text);

              &:checked {
                &::before {
                  content: '';
                  display: block;
                  width: 0.4em;
                  height: 0.8em;
                  margin-top: -0.2em;
                  border: 0 solid currentColor;
                  border-width: 0 2px 2px 0;
                  transform-origin: center;
                  transform: rotate(45deg);
                }
              }
            }
          }
        }
      }
    }
  }

  .page-footer-bottom {
    padding-block: 0.875rem;
    font-size: 0.75rem;

    @media (max-width: 576px) {
      flex-direction: column;
      gap: 1rem;
    }

    .footer-col {
      display: flex;
      align-items: center;
      gap: 2rem;

      .mk-logo {
        height: 1.125rem;
      }

      &:nth-child(2) {
        @media (max-width: 992px) {
          flex: 0.1;
        }
      }

      &:last-child {
        justify-content: flex-end;

        @media (max-width: 576px) {
          justify-content: center;
        }
      }

      @media (max-width: 576px) {
        justify-content: center;
      }
    }
  }
}
</style>
