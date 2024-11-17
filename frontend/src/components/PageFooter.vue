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
          <form class="newsletter-form">
            <div class="form-group">
              <label>
                Vpiši svoj e-naslov
                <input type="email" required id="newsletter-email" />
              </label>
            </div>
            <div class="form-group">
              <div class="checkbox">
                <input type="checkbox" required id="newsletter-checkbox" />
                <label for="newsletter-checkbox">
                  <span>
                    Strinjam se, da mi Danes je nov dan po e-pošti pošilja
                    Občasnik in druga obvestila.
                  </span>
                </label>
              </div>
            </div>
            <div class="form-group">
              <button type="submit" class="button-link submit-button">
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
              <img
                src="@/assets/img/min-za-kulturo.png"
                alt="Ministrstvo za kulturo logo"
                class="min-logo"
              />
            </div>
            <div class="footer-logo">
              <img
                src="@/assets/img/embassy-lj.png"
                alt="United states embassy in Ljubljana"
                class="embassy-logo"
              />
              <span>
                Projekt je bil delno financiran z donacijo veleposlaništva ZDA.
                Izražena mnenja, ugotovitve in sklepi ali priporočila pripadajo
                avtorjem in ne odražajo nujno mnenj Department of State.
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
      font-size: 0.75rem;

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
        padding: 0.6em 0.9em;
        background: #4063f6;
        border: 0.5px solid #000;
        border-radius: 3px;
        font-weight: 700;
        color: #fff;
        text-decoration: none;
      }

      .donate-link {
        margin-left: 0.75rem;
      }

      .submit-button {
        margin-top: 0.5rem;
      }

      .newsletter-form {
        margin-top: 1rem;

        .form-group {
          margin-top: 0.5rem;

          label {
            display: flex;
            flex-direction: column;
            font-size: 0.625rem;
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

          img {
            flex-shrink: 0;
            display: block;
            margin-inline: auto;

            @media (min-width: 768px) {
              margin-inline: 0;
            }

            &.min-logo {
              height: 1.25rem;
            }

            &.embassy-logo {
              height: 2.5rem;
            }
          }

          span {
            font-size: 0.4375rem;

            @media (min-width: 768px) {
              font-size: 0.5625rem;
            }
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
