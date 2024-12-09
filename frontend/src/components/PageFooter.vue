<script setup lang="ts">
import axios from 'axios'
import { ref } from 'vue'
import MkLogo from './logos/MkLogo.vue'
import UseLogo from './logos/UseLogo.vue'

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
    <div class="page-footer">
      <div>
        <div class="footer-block">
          Za <strong>Razkrinkaj.AI</strong> skrbi<br />
          <a
            href="https://danesjenovdan.si"
            target="_blank"
            rel="noopener noreferrer"
            class="about-link"
            >Danes je nov dan, Inštitut za druga vprašanja</a
          >
        </div>
        <hr />
        <div class="footer-block">
          Podpri naše delo.
          <a
            href="https://danesjenovdan.si/podpri-nas/"
            target="_blank"
            rel="noopener noreferrer"
            class="button-link donate-link"
          >
            <span>DONIRAJ</span>
            <span>❤</span>
          </a>
        </div>
        <hr />
      </div>
      <div>
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
      <hr />
      <div>
        <div class="footer-block">
          <div class="footer-logos">
            <div class="footer-logo">
              <MkLogo />
            </div>
            <div class="footer-logo">
              <UseLogo />
              <span>
                Projekt je bil delno financiran z donacijo Veleposlaništva ZDA v
                Ljubljani. Izražena mnenja, ugotovitve, sklepi ali priporočila
                pripadajo avtorjem in ne odražajo nujno mnenj Ministrstva za
                zunanje zadeve ZDA.
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped lang="scss">
footer {
  margin-inline: calc(var(--page-gutter) * -1);
  padding-inline: var(--page-gutter);
  background: var(--color-bg-white);

  .page-footer {
    margin-inline: auto;
    width: var(--footer-width);

    @media (min-width: 768px) {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      column-gap: 2.75rem;
      padding-block: 0.75rem;

      & > hr {
        display: none;
      }

      & > :last-child {
        grid-column: 1 / -1;
      }
    }

    @media (min-width: 992px) {
      grid-template-columns: repeat(3, 1fr);

      & > :last-child {
        grid-column: initial;
      }
    }

    .footer-block {
      padding-block: 1.25rem;
      font-size: 0.875rem;

      strong {
        font-weight: 700;
      }

      .semi-bold {
        font-weight: 600;
      }

      .about-link {
        font-weight: 600;
        color: #092bba;
      }

      .button-link {
        display: inline-flex;
        gap: 0.5em;
        align-items: center;
        padding: 0.4em 0.62em 0.3em;
        background: #4063f6;
        border: 0.5px solid #000;
        border-radius: 3px;
        font-weight: 700;
        line-height: 1.3;
        color: #fff;
        text-decoration: none;

        &:hover {
          background: #3458f3;
          box-shadow:
            0px 0px 4px 0px #173ac9 inset,
            0px 0px 5px -1px #4063f6;
        }
      }

      .donate-link {
        margin-left: 0.75rem;
      }

      .submit-button {
        margin-top: 0.5rem;

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
            font-weight: 300;

            input {
              margin-top: 0.25rem;
              padding: 0.3em 0.6em;
              background: #f3f3ec;
              border: 0.5px solid #545454;
              border-radius: 5px;
              font-weight: 400;
              font-size: 1rem;
              line-height: 1rem;
            }
          }

          .checkbox {
            display: flex;
            gap: 0.5em;

            input[type='checkbox'] {
              appearance: none;
              display: grid;
              place-items: center;
              background: #f3f3ec;
              margin: 0;
              flex-shrink: 0;
              width: 1.5rem;
              height: 1.5rem;
              border: 0.5px solid #545454;
              border-radius: 5px;

              &:checked {
                &::before {
                  content: '';
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
            }
          }
        }
      }

      .footer-logos {
        display: grid;
        gap: 1rem;

        @media (min-width: 768px) {
          gap: 1.75rem;
          display: flex;
          justify-content: center;
        }

        @media (min-width: 992px) {
          display: grid;
          justify-content: initial;
        }

        .footer-logo {
          display: flex;
          gap: 0.75rem;
          align-items: center;
          max-width: 260px;
          margin-inline: auto;

          @media (min-width: 768px) {
            margin-inline: 0;
          }

          svg {
            flex-shrink: 0;
          }

          .mk-logo {
            height: 1.25rem;
          }

          .embassy-logo {
            height: 2.5rem;
          }

          span {
            font-size: 0.5625rem;
          }
        }
      }
    }

    hr {
      margin: 0;
      height: 3px;
      border: none;
      background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20.15 9"><path fill="none" stroke="%23A0B1FB" stroke-width="2" d="M0 1c5.04 0 5.04 7 10.08 7s5.03-7 10.07-7"/></svg>');
      background-repeat: repeat-x;
      background-position: left center;
      background-size: auto 100%;
    }
  }
}
</style>
