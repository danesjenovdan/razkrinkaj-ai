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
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 178.115 26.173"
                class="mk-logo"
                alt="Republika Slovenija - Ministrstvo za kulturo"
              >
                <path
                  d="M42.549 16.16v8.114h1.382v-5.995h.056l1.395 3.15h1.337l1.383-3.162h.056v6.007h1.428v-8.115h-1.824l-1.632 3.683h-.057l-1.643-3.683zm10.313 0h-1.576v8.114h1.576zm5.916 8.114h2.096v-8.115h-1.405v6.268h-.056L56.67 16.16h-2.085v8.115h1.405v-6.087h.056zm5.395-8.115h-1.575v8.115h1.575zm6.612 4.834a1.624 1.624 0 0 0-.379-.644 2.182 2.182 0 0 0-.692-.464 8.219 8.219 0 0 0-1.053-.375 6.814 6.814 0 0 1-.63-.203 1.903 1.903 0 0 1-.448-.237.859.859 0 0 1-.272-.33 1.116 1.116 0 0 1-.09-.474c0-.188.03-.34.09-.452a.677.677 0 0 1 .25-.267.95.95 0 0 1 .374-.124c.143-.018.302-.03.476-.03a5.314 5.314 0 0 1 1.927.365l.192-1.312a6.236 6.236 0 0 0-1.053-.32 5.607 5.607 0 0 0-1.1-.103c-.922 0-1.618.178-2.086.534-.468.354-.702.962-.702 1.824 0 .393.05.724.153.992.101.268.25.496.441.685.194.19.434.345.72.47.287.125.616.24.987.346.264.076.483.15.657.221.174.072.314.15.419.238a.757.757 0 0 1 .227.3c.045.114.068.25.068.408a1.2 1.2 0 0 1-.096.51.764.764 0 0 1-.267.318c-.113.076-.25.128-.408.158a2.75 2.75 0 0 1-.521.046c-.355 0-.726-.034-1.111-.102a7.038 7.038 0 0 1-1.043-.261l-.282 1.36c.332.105.689.19 1.07.25.382.06.807.09 1.275.09.544 0 1.007-.045 1.388-.136.381-.09.696-.236.941-.436a1.68 1.68 0 0 0 .532-.77c.11-.311.166-.694.166-1.147 0-.37-.04-.68-.12-.928m6.364-3.462V16.16h-5.814v1.372h2.119v6.743h1.576V17.53zm6.624 0a1.71 1.71 0 0 0-.471-.76c-.219-.204-.513-.357-.884-.458-.37-.103-.83-.154-1.383-.154h-2.798v8.115h1.574V21.09h1.202l1.576 3.184h1.813l-1.79-3.423c.46-.181.793-.464.997-.85.204-.386.305-.86.305-1.427 0-.393-.047-.741-.141-1.043m-1.53 1.643a.727.727 0 0 1-.216.363.937.937 0 0 1-.418.198 3.045 3.045 0 0 1-.675.063h-1.123v-2.29h1.123c.507 0 .861.075 1.065.227.204.15.306.446.306.883 0 .22-.02.405-.062.556m8.126 1.819a1.612 1.612 0 0 0-.38-.644 2.16 2.16 0 0 0-.691-.464 8.247 8.247 0 0 0-1.055-.375 6.908 6.908 0 0 1-.628-.203 1.851 1.851 0 0 1-.448-.237.859.859 0 0 1-.272-.33 1.097 1.097 0 0 1-.09-.474c0-.188.029-.34.09-.452a.668.668 0 0 1 .25-.267.95.95 0 0 1 .373-.124c.144-.018.303-.03.476-.03a5.339 5.339 0 0 1 1.927.365l.193-1.312a6.248 6.248 0 0 0-1.055-.32 5.603 5.603 0 0 0-1.098-.103c-.923 0-1.618.178-2.086.534-.469.354-.702.962-.702 1.824 0 .393.05.724.153.992.101.268.25.496.441.685.194.19.432.345.72.47.287.125.616.24.986.346.265.076.484.15.657.221.175.072.313.15.42.238a.757.757 0 0 1 .227.3c.045.114.068.25.068.408a1.2 1.2 0 0 1-.096.51.773.773 0 0 1-.267.318c-.113.076-.25.128-.408.158a2.76 2.76 0 0 1-.521.046c-.356 0-.726-.034-1.111-.102a7.038 7.038 0 0 1-1.043-.261l-.284 1.36c.334.105.69.19 1.072.25.382.06.806.09 1.275.09.544 0 1.007-.045 1.388-.136.381-.09.695-.236.941-.436a1.68 1.68 0 0 0 .532-.77c.11-.311.164-.694.164-1.147 0-.37-.038-.68-.118-.928m6.364-3.462V16.16h-5.815v1.372h2.12v6.743h1.575V17.53zm7.218-1.372h-1.597l-1.735 6.744h-.056l-1.722-6.744h-1.667l2.199 8.115h2.369Zm5.316 8.059c.415-.13.759-.353 1.031-.675.272-.321.475-.752.607-1.292s.198-1.222.198-2.045c0-.81-.068-1.481-.204-2.019-.136-.536-.342-.964-.617-1.285a2.23 2.23 0 0 0-1.032-.68c-.412-.132-.893-.199-1.445-.199-.559 0-1.047.067-1.462.199-.416.132-.761.36-1.037.685-.276.326-.481.758-.617 1.298s-.204 1.218-.204 2.034c0 .816.068 1.492.204 2.028.136.538.341.964.617 1.282.276.317.621.54 1.037.669.415.128.903.192 1.462.192.56 0 1.046-.064 1.462-.192m-2.294-1.321a1.079 1.079 0 0 1-.511-.47c-.124-.22-.212-.512-.26-.878-.05-.367-.075-.82-.075-1.355 0-.544.026-.996.075-1.355.048-.358.136-.645.26-.861.125-.215.295-.367.51-.453.215-.087.489-.131.822-.131.332 0 .607.044.821.13.216.087.386.24.511.454.124.216.21.503.26.861.05.359.073.81.073 1.355 0 .536-.024.988-.073 1.355-.05.366-.136.658-.26.878a1.079 1.079 0 0 1-.51.47c-.215.094-.49.142-.822.142-.333 0-.607-.048-.821-.142m13.094 1.377v-1.348h-3.75l3.672-5.407v-1.36h-5.226v1.35h3.458l-3.627 5.382v1.383zm5.916 0h1.7l-2.47-8.115h-2.12l-2.459 8.115h1.655l.453-1.71h2.765zm-1.893-6.687h.057l.998 3.65h-2.04zm7.016 6.687h1.575v-3.559h.42l2.232 3.559h1.858l-2.798-4.25 2.674-3.865H135.3l-2.165 3.287h-.453v-3.287h-1.575Zm11.321-8.115v5.168c0 .332-.03.608-.09.828-.06.219-.154.395-.278.527a1.01 1.01 0 0 1-.47.277c-.19.054-.412.08-.668.08a2.37 2.37 0 0 1-.652-.08 1.013 1.013 0 0 1-.466-.277 1.28 1.28 0 0 1-.282-.544 3.41 3.41 0 0 1-.096-.89v-5.089h-1.576v5.259c0 .544.068 1.005.204 1.383.137.377.333.685.59.924.258.237.576.412.955.52.377.11.805.165 1.283.165.992 0 1.76-.237 2.305-.713.544-.476.817-1.251.817-2.324v-5.214zm8.15 8.115v-1.37h-3.378v-6.745h-1.576v8.115zm5.314-6.743V16.16h-5.813v1.372h2.119v6.743h1.576V17.53zm5.576-1.372v5.168c0 .332-.03.608-.09.828-.06.219-.154.395-.278.527a1.01 1.01 0 0 1-.47.277c-.19.054-.412.08-.668.08a2.37 2.37 0 0 1-.652-.08 1.013 1.013 0 0 1-.466-.277 1.28 1.28 0 0 1-.282-.544 3.41 3.41 0 0 1-.096-.89v-5.089h-1.576v5.259c0 .544.068 1.005.204 1.383.136.377.333.685.59.924.258.237.575.412.954.52.378.11.806.165 1.284.165.99 0 1.76-.237 2.304-.713.545-.476.817-1.251.817-2.324v-5.214zm8.732 1.372a1.71 1.71 0 0 0-.47-.76c-.219-.204-.514-.357-.884-.458-.37-.103-.831-.154-1.383-.154h-2.799v8.115h1.575V21.09h1.201l1.576 3.184h1.814l-1.791-3.423c.461-.181.793-.464.997-.85.204-.386.306-.86.306-1.427a3.48 3.48 0 0 0-.142-1.043m-1.529 1.643a.737.737 0 0 1-.216.363.937.937 0 0 1-.419.198 3.053 3.053 0 0 1-.674.063h-1.123v-2.29h1.123c.506 0 .861.075 1.065.227.204.15.305.446.305.883 0 .22-.02.405-.061.556m7.61 5.044a2.16 2.16 0 0 0 1.031-.675c.272-.321.474-.752.607-1.292.132-.54.197-1.222.197-2.045 0-.81-.068-1.481-.204-2.019-.136-.536-.341-.964-.617-1.285a2.232 2.232 0 0 0-1.03-.68c-.413-.132-.895-.199-1.446-.199-.56 0-1.047.067-1.463.199-.414.132-.761.36-1.036.685-.276.326-.482.758-.618 1.298s-.204 1.218-.204 2.034c0 .816.068 1.492.204 2.028.136.538.342.964.618 1.282.275.317.622.54 1.036.669.416.128.903.192 1.463.192.559 0 1.047-.064 1.461-.192m-2.294-1.321a1.076 1.076 0 0 1-.51-.47c-.125-.22-.212-.512-.261-.878-.05-.367-.073-.82-.073-1.355 0-.544.024-.996.073-1.355.05-.358.136-.645.261-.861.124-.215.295-.367.51-.453.216-.087.489-.131.821-.131.333 0 .607.044.823.13.214.087.385.24.509.454.125.216.212.503.261.861.048.359.074.81.074 1.355 0 .536-.026.988-.074 1.355-.049.366-.136.658-.261.878a1.076 1.076 0 0 1-.51.47c-.215.094-.489.142-.822.142-.332 0-.605-.048-.821-.142M43.693 7.15h1.803l1.813 3.523h.986L46.403 7.06c.588-.106 1.022-.34 1.302-.698.28-.358.42-.881.42-1.57 0-.415-.053-.766-.16-1.054a1.515 1.515 0 0 0-.492-.69 2.09 2.09 0 0 0-.844-.374 5.565 5.565 0 0 0-1.201-.114h-2.596v8.114h.861zm0-3.865h1.666c.318 0 .596.02.833.063.239.041.435.119.59.232.154.115.271.272.351.472.079.201.119.465.119.79 0 .334-.041.606-.124.814-.084.21-.204.37-.364.484-.157.113-.355.19-.59.227a5.055 5.055 0 0 1-.815.057h-1.666zm11.072 7.388V9.95h-4V6.945h3.468V6.22h-3.468V3.285h4V2.56h-4.861v8.114zm2.584-3.342h1.678c.929 0 1.612-.187 2.046-.562.434-.373.651-1.002.651-1.886 0-.44-.052-.806-.159-1.1a1.592 1.592 0 0 0-.492-.714 2.06 2.06 0 0 0-.845-.39 5.29 5.29 0 0 0-1.201-.12h-2.539v8.114h.861zm0-4.024h1.61c.317 0 .596.02.833.062.239.043.435.124.59.246.154.12.271.288.351.5.079.212.119.489.119.83 0 .356-.041.643-.125.859a1.085 1.085 0 0 1-.363.5 1.377 1.377 0 0 1-.59.239 4.724 4.724 0 0 1-.815.062h-1.61zm11.164-.748h-.861v5.326c0 .77-.164 1.327-.493 1.667-.328.34-.818.51-1.468.51-.658 0-1.147-.169-1.467-.505-.321-.336-.483-.893-.483-1.672V2.56h-.861v5.417c0 .99.24 1.71.72 2.16.48.45 1.157.673 2.035.673a3.96 3.96 0 0 0 1.212-.17c.356-.112.657-.288.906-.526.25-.238.439-.544.567-.918.13-.374.193-.822.193-1.343zm7.078 4.637c-.186-.3-.475-.524-.867-.676v-.045c.664-.28.997-.883.997-1.811 0-.701-.2-1.228-.601-1.579-.4-.35-1.057-.526-1.972-.526h-2.584v8.114h2.584c.96 0 1.653-.177 2.08-.533.427-.355.64-.915.64-1.679 0-.545-.092-.966-.277-1.265m-1.003 2.383c-.272.246-.688.37-1.247.37h-1.916V6.9h1.916c.559 0 .975.122 1.247.365.272.243.408.625.408 1.15 0 .53-.136.918-.408 1.165m-.17-3.716c-.287.208-.68.312-1.18.312h-1.813v-2.89h1.814c.506 0 .901.102 1.185.306.283.204.424.585.424 1.144 0 .544-.143.92-.43 1.128m7.842 4.81V9.95h-3.785V2.56h-.862v8.114zm2.267-8.114h-.862v8.114h.862zm2.244 8.114h.861V6.877h.703l2.72 3.796h1.042L89.095 6.48l2.934-3.921h-.997l-2.64 3.58h-.76V2.56h-.861zm11.514 0h.907L96.517 2.56h-1.156l-2.664 8.114h.884l.624-1.982h3.446zm-2.38-7.344h.046l1.473 4.636h-2.992zm11.623 4.336a1.472 1.472 0 0 0-.375-.624 2.458 2.458 0 0 0-.73-.476c-.311-.14-.703-.285-1.179-.436a5.99 5.99 0 0 1-.692-.238 1.73 1.73 0 0 1-.487-.295 1.043 1.043 0 0 1-.289-.419 1.754 1.754 0 0 1-.096-.624c0-.49.127-.841.38-1.053.252-.212.681-.317 1.285-.317.348 0 .67.03.964.09.295.06.596.144.907.25l.147-.726a5.327 5.327 0 0 0-.991-.277 5.916 5.916 0 0 0-1.06-.097c-.861 0-1.496.184-1.904.55-.408.367-.612.912-.612 1.638 0 .34.045.633.136.878.09.246.228.459.413.64.186.182.42.335.703.459.284.125.613.24.992.347.34.097.621.196.844.293.223.099.4.21.533.335a.973.973 0 0 1 .272.442c.048.17.074.372.074.606 0 .288-.035.525-.103.714a.974.974 0 0 1-.31.448c-.14.11-.317.186-.529.227a4.01 4.01 0 0 1-.758.061 6.455 6.455 0 0 1-2.143-.362l-.181.737c.34.128.688.223 1.042.283.356.06.748.09 1.179.09.484 0 .896-.041 1.236-.124a2.01 2.01 0 0 0 .833-.397 1.52 1.52 0 0 0 .464-.708c.095-.29.142-.64.142-1.048 0-.34-.036-.63-.107-.867m6.352 3.008V9.95h-3.785V2.56h-.862v8.114zm5.088-.073c.393-.14.716-.373.97-.703.253-.328.442-.761.566-1.297.125-.536.187-1.201.187-1.995 0-.778-.064-1.436-.192-1.972-.13-.536-.322-.966-.579-1.292a2.168 2.168 0 0 0-.968-.702c-.39-.144-.845-.216-1.367-.216-.528 0-.989.072-1.382.216-.392.144-.718.38-.975.708-.256.329-.45.764-.577 1.304-.13.54-.194 1.202-.194 1.988s.064 1.445.194 1.978c.128.532.321.962.577 1.286.257.325.583.557.975.697.393.14.854.21 1.382.21.53 0 .991-.07 1.383-.21m-2.453-.736a1.503 1.503 0 0 1-.68-.601c-.17-.276-.291-.632-.363-1.071-.072-.439-.108-.97-.108-1.599 0-.634.036-1.168.108-1.602.072-.435.193-.787.363-1.055.17-.268.397-.46.68-.577.284-.118.636-.176 1.06-.176.422 0 .776.058 1.06.176.282.117.509.309.68.577.169.268.29.62.362 1.055.071.434.107.968.107 1.602 0 .628-.036 1.16-.107 1.599-.072.439-.193.795-.362 1.07a1.502 1.502 0 0 1-.68.602c-.284.124-.638.187-1.06.187-.424 0-.776-.063-1.06-.187m7.349.81h1.213l2.436-8.115h-.838l-2.154 7.276h-.045L122.3 2.559h-.884zm9.747 0V9.95h-4V6.945h3.468V6.22h-3.468V3.285h4V2.56h-4.862v8.114zm6.21 0h1.259V2.558h-.793v7.186h-.046l-3.638-7.186h-1.27v8.114h.794V3.477h.045zm4.364-8.115h-.861v8.114h.861zm2.482 0v7.537c0 .28-.023.525-.068.736a1.533 1.533 0 0 1-.232.556c-.11.159-.252.293-.426.403-.173.109-.389.2-.646.277l.226.725c.386-.113.707-.25.964-.408a2.08 2.08 0 0 0 .618-.566c.154-.22.265-.476.329-.771a4.84 4.84 0 0 0 .096-1.02v-7.47Zm7.56 8.114h.906L152.46 2.56h-1.156l-2.664 8.114h.884l.624-1.982h3.445zm-2.38-7.344h.045l1.473 4.636h-2.992z"
                />
                <path
                  fill="#5f9db7"
                  d="M20.121 14.17c-.352 5.62-4.134 10.406-9.686 12.003-5.351-1.516-9.335-6.2-9.7-12.002L0 2.517C3.401.868 6.565 0 10.435 0c3.5 0 6.969.768 10.42 2.517m-1.486.168-.716 11.387c-.3 4.75-3.384 8.968-8.218 10.568a11.854 11.854 0 0 1-8.219-10.568L1.481 2.685c-.184.082-.468.198-.665.3l.7 11.135c.335 5.237 3.919 9.772 8.919 11.24 4.902-1.468 8.584-5.903 8.918-11.24l.7-11.135a12.719 12.719 0 0 0-.684-.3M8.301 13.356 6.82 11.371 3.3 16.089c.25 1.216.847 1.8 2.334 1.8 1.017 0 1.184-.634 2.382-.634 1.25 0 1.335.634 2.418.634 1.052 0 1.149-.634 2.401-.634 1.252 0 1.365.634 2.399.634 1.469 0 2.152-.7 2.336-1.816l-3.535-4.702-1.484 1.985-2.117-4.235Zm6.934 6.183c.336 0 .636-.066.901-.182.199-.317.332-.566.503-.901-.418.219-.868.385-1.404.385-1.168 0-1.232-.634-2.399-.634-1.117 0-1.268.634-2.417.634-1.186 0-1.2-.634-2.402-.634-1.133 0-1.266.634-2.401.634-.63 0-1.033-.236-1.417-.42.168.335.352.636.552.954.281.098.582.148.884.148 1.23 0 1.214-.634 2.382-.634 1.118 0 1.267.65 2.402.65 1.165 0 1.3-.65 2.417-.65 1.115 0 1.252.65 2.399.65m-2.399.3c-1.1 0-1.135.649-2.401.649-1.184 0-1.4-.65-2.418-.65-1.065 0-1.082.62-2.448.635a11.302 11.302 0 0 0 4.866 3.351 11.006 11.006 0 0 0 4.852-3.35c-1.336 0-1.37-.635-2.451-.635m-5.3-17.404-.901-.084.533.716-.55.734.918-.098.365.833.368-.833.916.098-.55-.734.532-.731-.898.099-.368-.834Zm2.533 3.368-.902-.083.533.717-.55.734.92-.102.365.835.368-.835.916.102-.551-.734.533-.734-.898.1-.368-.834zm2.516-3.368-.901-.084.536.716-.552.734.917-.098.367.833.368-.833.917.098-.552-.734.534-.731-.899.099-.368-.834Z"
                />
              </svg>
            </div>
            <div class="footer-logo">
              <img
                src="data:file/png;base64,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"
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
      }

      .donate-link {
        margin-left: 0.75rem;
      }

      .submit-button {
        margin-top: 0.5rem;
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
