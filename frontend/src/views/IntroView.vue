<script setup lang="ts">
import { useStore } from '@/stores/store'
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import PageFooter from '@/components/PageFooter.vue'

const store = useStore()

const scrollToMore = () => {
  document
    .querySelector('a[name="more"]')
    ?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <main>
    <div class="page-gutter bg-manipulacija-color-3">
      <div class="intro">
        <h1>
          <img
            src="/manipulacija-logo.svg"
            alt="Manipulacija ni informacija"
            class="title-logo"
          />
        </h1>
        <div class="narrow">
          <div class="description" v-html="store.introductionDescription"></div>
          <ButtonPrimary
            class="button"
            :buttonText="store.introductionButtonText"
            :link="{ name: 'chapter-list' }"
            icon="hands"
          />
          <ButtonPrimary
            class="button"
            :buttonText="store.introductionButtonTextSecondary"
            href="#more"
            color="secondary"
            side-icon="hand-down"
            @click.prevent="scrollToMore"
          />
        </div>
      </div>
    </div>
    <div class="page-gutter bg-manipulacija-color-7">
      <div class="explanations">
        <a name="more"></a>
        <h2>SPOZNAJ MANIPULACIJSKE TAKTIKE</h2>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi cumque
        numquam quaerat maiores accusantium enim asperiores, dolore eveniet
        cupiditate in soluta aliquid, est omnis. Repellendus, dolorem corporis.
        Molestias, nostrum deleniti.

        <div class="content">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Deleniti
          animi natus suscipit exercitationem? Delectus doloremque quasi non
          molestias, quae nobis exercitationem ipsa? Quos voluptatum nihil alias
          necessitatibus dolorum tenetur dolorem? Explicabo laudantium eum
          perferendis voluptatibus deserunt. Sed facere fuga aliquam. Sint omnis
          corrupti a ab, at reprehenderit voluptatibus quidem aperiam deserunt
          eveniet ratione odio cupiditate neque quaerat sequi recusandae atque!
          Perferendis cumque voluptatibus labore mollitia ratione porro, alias
          commodi libero, nisi ipsam aperiam molestiae delectus pariatur dolore
          minus omnis nobis ex! Veniam illum unde facere voluptatibus fugiat
          dolor maxime cumque. Unde, dolores? Facere laudantium molestiae,
          soluta illum animi ex dolor accusamus quidem unde nobis eaque,
          consequuntur nostrum incidunt? Quia, officiis minima! Perferendis
          inventore voluptate rem quo, fuga esse maxime numquam! Debitis fugit
          eveniet expedita voluptas, repellat corporis consequuntur quae
          accusantium, soluta odio culpa aperiam incidunt, voluptates nobis
          alias doloremque. Ea a perferendis, quos repellendus beatae asperiores
          assumenda pariatur corporis dolore. Voluptas illum esse quasi
          temporibus praesentium similique, illo quod, repellendus modi
          perspiciatis provident. Dicta, praesentium possimus earum quos laborum
          consectetur numquam vero harum, sit beatae adipisci fuga, animi
          voluptatum? Porro. Optio, sequi adipisci cum voluptatem facilis fuga
          vel, rem neque impedit fugit tenetur est similique! Incidunt neque
          nemo dicta modi qui deleniti sint, itaque dolor, architecto delectus
          quo. Assumenda, laboriosam? Nesciunt est alias earum voluptas
          aspernatur pariatur itaque fugiat impedit eum obcaecati voluptate
          quisquam ex corrupti soluta quae repellendus quam expedita facilis
          perferendis ab reiciendis quis, dolorem hic. Soluta, voluptatum? Saepe
          quam, officia dolore voluptatum a esse sapiente assumenda rem quisquam
          harum inventore eum eveniet deleniti praesentium possimus. Cupiditate
          velit amet placeat, est deserunt quos ullam. Quae facere vitae unde!
          Rerum necessitatibus soluta dolore. Sed unde tempora quo assumenda est
          sapiente, possimus eius, molestias ullam quis ut, inventore quae
          exercitationem libero odio blanditiis necessitatibus voluptatum fuga.
          Quia sapiente iusto nemo. Ab non eos assumenda. Quia minus dolorem
          adipisci repellat, sequi eaque laborum blanditiis! Odit, consequuntur!
          Libero perspiciatis animi distinctio ullam cumque assumenda minus
          tenetur, blanditiis facere eligendi. Aperiam, accusantium quam! Iure
          ipsam exercitationem pariatur animi aliquid aut error amet excepturi
          ipsum sed a provident voluptates nihil, doloremque, alias esse. Sint
          saepe vel alias aspernatur consectetur molestiae deleniti odit minus
          porro. Placeat ratione nulla ut dignissimos laborum, optio atque
          autem! Aliquid perspiciatis vel quos suscipit architecto at
          reiciendis, quo laborum sunt veritatis nisi, rem perferendis cumque
          accusamus delectus unde explicabo neque? Dignissimos rerum sapiente
          cumque facere nulla molestiae maiores obcaecati quisquam iure, dolor
          amet fuga non fugit in eum provident labore quia ut eligendi aut totam
          ipsam. Cupiditate dolor dignissimos ipsum. Eaque sed culpa officiis
          nostrum! In commodi distinctio, maiores sunt voluptates numquam cumque
          sequi recusandae fuga, saepe aspernatur, illum minima debitis incidunt
          nobis harum aut delectus quibusdam dolor sint pariatur? Esse
          temporibus quasi laborum consequatur expedita optio quas facilis
          commodi delectus labore velit distinctio asperiores autem reiciendis,
          voluptas ea ut earum ab. Nemo amet maiores ad, neque quaerat nobis?
          Veniam. Aut molestias amet suscipit sint minus perferendis aspernatur
          animi et ratione explicabo rem unde doloremque voluptatem nulla, nisi,
          consectetur quasi quis, facilis totam. Provident quia modi distinctio
          ipsum corporis repellat! Eveniet impedit amet dolore corporis dolores
          voluptas non nihil quas velit neque ut optio, nesciunt maiores eaque,
          dolorum aut facere iusto sit id, cumque quod sed omnis! Eius, quae
          corrupti? Tempore praesentium officia error, pariatur incidunt sequi
          necessitatibus in. Esse consequuntur consequatur soluta corrupti
          dolore maiores dolores! Magnam repellat, illum nostrum voluptates
          error vel culpa dicta laboriosam temporibus itaque optio. Ratione
          repellendus odit, in dolor numquam itaque nam natus saepe delectus.
          Quas sapiente aspernatur modi voluptates beatae voluptatibus doloribus
          sunt rem impedit, aliquam porro hic blanditiis rerum natus! Fugiat,
          aperiam. Exercitationem a tempore ullam reiciendis repellendus
          adipisci recusandae dolores quos rerum voluptate minus illum
          laudantium, hic ad eligendi ducimus, tenetur esse provident quia,
          alias quae atque. Quasi sunt sit totam! Maxime asperiores explicabo
          officiis dolorum quas blanditiis aliquam ducimus voluptatem
          necessitatibus atque molestias qui, eius vel, cupiditate consequuntur
          nisi, animi tempora quos corrupti. Animi, deleniti exercitationem
          doloremque aut dolores numquam. Nesciunt, voluptates similique amet
          sint atque, ea itaque aspernatur tempora vitae facere harum optio!
          Vitae consequatur ipsa vel temporibus aliquid molestiae eligendi
          officiis aut laboriosam incidunt, veritatis unde repellendus nesciunt!
          Asperiores dolore, cumque omnis, eligendi temporibus similique ea
          consectetur dolorum quaerat animi, impedit nisi. Perspiciatis est qui
          asperiores velit possimus voluptatum sint nesciunt aliquid modi,
          incidunt molestiae at cumque nobis! Recusandae accusamus quisquam
          voluptatibus iusto in maiores ut velit eaque tempore quae laborum
          voluptas sed maxime ipsum itaque neque odio eos exercitationem porro
          excepturi natus nostrum sint, sunt eveniet. Temporibus! Distinctio est
          recusandae aspernatur error architecto corporis quas. Commodi neque
          vero fugiat, est numquam quod ad atque earum quasi saepe. Quasi
          quisquam non delectus eos a quod quo itaque exercitationem! Sed veniam
          asperiores nesciunt non nobis veritatis aperiam sequi, quidem a quod
          error pariatur, adipisci laboriosam optio beatae! Minima, suscipit
          delectus velit dicta repudiandae corrupti voluptates tempore corporis
          provident? Tempora! Nisi dolores voluptas ea ut rem quos facere. Cum
          laborum molestias quibusdam est! Molestiae, architecto, ut
          exercitationem modi ullam quos eos quam harum reprehenderit natus ad
          error eum necessitatibus eaque. Illum amet perferendis laudantium
          magnam. Delectus repellat illo id praesentium minus veniam
          reprehenderit magni corrupti hic, voluptatum iure, earum quas.
          Veritatis, hic. Aspernatur explicabo, odio magni placeat accusantium
          quaerat modi? Odio sunt, amet quasi deleniti, tenetur eum dolorem in
          eaque, labore sint libero architecto. Possimus rerum, aut, suscipit
          magnam eum ipsam doloremque, ab aliquid blanditiis ullam ipsa iste
          saepe commodi? Repellendus doloribus laboriosam nostrum eaque
          excepturi ipsa libero rem saepe, incidunt illo deserunt veritatis,
          sunt sequi? Deleniti doloremque facere, iusto necessitatibus hic
          eligendi, nulla autem modi impedit tenetur, architecto est.
          Repudiandae, non nobis! Qui nihil sunt officia quisquam iure, aperiam
          esse? Minus consectetur aspernatur doloribus maiores dolorem quo
          dolorum enim unde, exercitationem mollitia accusantium numquam id
          libero quasi laboriosam facere! Sit maiores magni voluptatibus
          inventore ullam, voluptatem ipsa neque vitae distinctio aperiam
          consequuntur sed repellendus corporis similique expedita perspiciatis
          aliquam! Aspernatur, commodi? Ex totam quidem hic! Repellat a
          molestiae tempore. A aperiam eaque quis maiores. Delectus praesentium
          rerum rem placeat exercitationem distinctio, dolorem, aspernatur ut
          commodi nisi obcaecati et voluptates possimus veniam voluptatibus
          libero, amet corporis quod cum. Inventore, reprehenderit! Aliquid
          tempora minima ipsam iste expedita repudiandae eligendi molestias amet
          harum maiores reprehenderit deserunt animi, facere, quaerat tenetur
          corporis a doloremque porro excepturi accusantium vitae quia inventore
          commodi dolore. Adipisci. Tenetur quia magni incidunt repudiandae
          sapiente facilis itaque quasi, nostrum enim earum in inventore illo
          impedit, voluptatibus corrupti illum aperiam distinctio suscipit, esse
          odio rerum aspernatur. Saepe cum amet quos. Inventore voluptate maxime
          deleniti. Odio quod, labore error minus quam esse nostrum! Porro
          voluptates earum perferendis natus, quam architecto! Quo eum expedita
          porro tenetur necessitatibus laborum recusandae magnam corrupti sunt.
          Laboriosam nobis rem ipsam ab et tempora veniam obcaecati, minus cum
          suscipit fugit itaque. Vel ab nihil ipsam amet maiores hic
          accusantium, odio quibusdam quisquam nisi architecto, fugiat, illo
          eos? Quibusdam, magni vero. Officia ipsam sequi iure id, ratione enim
          hic facere quis architecto expedita dignissimos numquam. Velit
          deleniti ab nemo dolorem similique beatae! Deserunt atque natus
          facilis quibusdam aliquam. Velit excepturi incidunt saepe cumque, non
          nulla explicabo eveniet eos mollitia. Voluptas alias, sunt fuga velit
          necessitatibus id quaerat illo corporis deserunt sequi? Corrupti nobis
          qui beatae et odit eos. Praesentium blanditiis ab officia excepturi
          quam accusamus odit quia consequuntur nihil suscipit tempora quos
          minus, sint amet nisi. Dolorem sapiente, molestiae repudiandae
          pariatur eos vel. Ab fugit molestiae suscipit aut! Laborum aliquam
          numquam nihil eligendi corporis quaerat alias praesentium quae hic
          obcaecati delectus, mollitia omnis exercitationem? Assumenda et
          veritatis totam atque esse. Fugit, cum. Porro facilis neque fugit
          possimus incidunt! Debitis blanditiis earum vel animi amet non
          aspernatur asperiores ducimus rerum exercitationem alias laudantium
          quis, modi, inventore quaerat ut architecto molestiae eum dolore porro
          molestias numquam dolor! Mollitia, error blanditiis. Obcaecati dicta
          sint cupiditate necessitatibus molestiae laudantium asperiores optio
          officiis ducimus eum aspernatur tempora error est deleniti quas ab,
          labore totam modi ut repudiandae unde pariatur consectetur cumque?
          Quaerat, recusandae? Maiores quae, adipisci consectetur consequuntur
          laborum recusandae rerum pariatur quibusdam doloremque quam. Quidem,
          nobis et necessitatibus assumenda impedit quia! Autem, repudiandae
          obcaecati atque aliquid labore porro voluptate dignissimos ab culpa!
          Facere atque quasi labore ullam impedit nisi. Ad id delectus, sapiente
          consequatur vel saepe, mollitia placeat labore quam voluptatem qui
          perferendis pariatur harum quo quibusdam voluptatibus beatae
          exercitationem dolores iusto! Eaque sunt ipsum molestiae vero illum
          itaque eius rem assumenda laborum iure nostrum ipsam et, dolorem
          fugiat odit provident iusto dignissimos, debitis sequi cupiditate
          doloribus explicabo nam consequuntur. Quasi, delectus. Dolores vero
          eaque nobis assumenda? Inventore sint eveniet, exercitationem impedit
          aut ea magnam quo ipsum cupiditate porro, maxime accusamus voluptatum
          atque quis fugiat eos quam ducimus facere explicabo. Dolor, doloribus.
          Ab explicabo possimus perspiciatis ratione similique, libero beatae,
          labore incidunt debitis quasi officia hic quo dolorum iure laboriosam
          dolor? Dicta deserunt ipsam quidem accusamus eum earum nobis dolorem
          perspiciatis est. Non ab nobis iste ad aliquam saepe, voluptatum
          aperiam facilis veritatis odio vero nostrum incidunt quis. Praesentium
          vel similique ipsa aperiam amet consectetur maiores cumque. Hic
          provident velit distinctio nesciunt? Vero ipsam minus illo impedit
          quod error quaerat aperiam delectus deserunt pariatur. Quod magni
          natus corporis animi dolor quisquam officiis necessitatibus facilis
          earum ullam explicabo consectetur, deleniti tempora quo neque. Iure
          ipsa aut voluptas rerum maxime corrupti porro, accusamus nobis earum
          possimus delectus odio nam. Tenetur saepe dolor laboriosam libero
          perferendis, tempora ratione hic, iure, explicabo accusamus nulla!
          Numquam, fugiat. Quaerat molestias labore nobis inventore tempore
          maxime molestiae provident sed voluptatibus libero. Quisquam deserunt
          voluptate ipsam dolores, placeat fuga unde alias fugiat? Quos magni
          doloribus ullam asperiores cumque molestiae excepturi. Accusantium eum
          dolores perspiciatis tempora aut quos omnis assumenda reiciendis
          voluptas rem commodi, cumque quasi libero expedita alias porro
          deleniti impedit vero sint aliquid adipisci aspernatur magnam dolorum
          modi? Ad. Quia unde, corporis ab provident placeat autem saepe. Beatae
          magnam sint eius modi cumque quae nesciunt accusamus rerum blanditiis
          animi molestiae vero deserunt aut exercitationem quod omnis nam,
          doloribus id. Laborum velit quia libero pariatur non eius, neque amet
          odio quae accusantium fugiat necessitatibus commodi natus beatae
          repellat alias. Harum, quisquam? Similique expedita quia voluptates
          ullam iste, dolor adipisci obcaecati? Voluptate reprehenderit cum, non
          iste eius provident aperiam fuga voluptas ipsum at quibusdam
          doloremque delectus praesentium iusto facilis eaque optio ducimus qui
          necessitatibus, deleniti eligendi perferendis in natus maxime! Ipsam.
          Facere, fuga vitae porro quam quibusdam necessitatibus provident non
          eius quas. Sequi delectus, cumque itaque voluptates cum dolore
          consequuntur laboriosam tempora deleniti possimus? Aspernatur,
          explicabo. Tenetur nostrum sed ex dolorem. Omnis dolore sed quasi modi
          magni tenetur iusto fugiat harum consequatur? Neque consequuntur illum
          dicta temporibus natus, aperiam asperiores facere hic suscipit fuga
          dolores esse omnis voluptatem provident aut distinctio. Quasi odio
          deserunt cumque ducimus, quia aspernatur obcaecati culpa, id mollitia
          repellat ea, sint nobis! Facilis fuga ipsa repudiandae minima quae
          numquam in. Iusto quas alias voluptatem fugiat corrupti autem?
          Sapiente dolore voluptas doloribus voluptatum, expedita est maxime
          similique totam eum a odit, officiis architecto optio ut sunt.
          Blanditiis vero quis ipsa architecto molestiae fugiat repellendus
          tempore placeat quae dolor! Libero dicta numquam placeat eveniet
          reprehenderit eius error cumque exercitationem quibusdam optio
          inventore, maiores expedita assumenda esse architecto quam harum
          blanditiis ipsum accusantium. Voluptates mollitia qui illo pariatur?
          Illum, odio. Aperiam, dolorum. Obcaecati iure repudiandae corrupti
          quas culpa voluptate totam corporis, cupiditate illo nemo, quod
          suscipit dolores temporibus eius commodi voluptatem voluptatibus non
          exercitationem, quaerat fuga possimus qui veritatis! Aliquid. Saepe
          omnis, unde ipsam qui doloribus voluptate cupiditate voluptatum
          deserunt atque officiis iusto, soluta ducimus laborum aliquam debitis
          excepturi aspernatur, adipisci neque sequi animi illo esse! Officiis
          sed qui reprehenderit! Id modi voluptatum, repudiandae magnam illo
          fuga sapiente, laborum perspiciatis ea unde perferendis at labore
          eveniet necessitatibus consectetur tenetur ipsum recusandae
          reprehenderit mollitia iure quidem asperiores quis dolorum iste?
          Ratione? Quas blanditiis sapiente aut modi quis voluptatem perferendis
          iusto obcaecati harum labore inventore facere reiciendis fuga corrupti
          quo, nam itaque deleniti nostrum commodi, sint laboriosam dolores eum
          unde! Deserunt, quidem. Nisi explicabo suscipit eligendi ad excepturi
          atque? Soluta fugit cupiditate nisi illo? Sint, cum nobis. Iure
          inventore ullam aperiam, facere commodi omnis explicabo rerum
          molestias! Nihil quia tempora illo necessitatibus. Consectetur, error
          praesentium voluptates saepe suscipit modi quibusdam? Cupiditate
          tempora, sunt voluptatem consequatur pariatur ipsam enim officia
          excepturi, expedita deserunt eaque necessitatibus esse corrupti. Illum
          numquam quisquam doloremque in ut. Aut reiciendis ratione ullam nobis,
          consequuntur dolores eligendi minima adipisci quasi quibusdam? Beatae
          asperiores eius neque fugit debitis, laudantium facilis in, eum
          exercitationem dolore voluptatem corporis commodi aut vero expedita!
          Temporibus, fugiat fuga! Repellendus, explicabo quam adipisci tempore
          fugiat, sed veritatis nihil enim non natus dolore laborum incidunt
          repellat debitis. Accusantium id ipsa ut veritatis voluptatum nostrum!
          Commodi, veniam delectus. Molestias quod perspiciatis, assumenda
          temporibus expedita esse odio excepturi quis nisi rerum quibusdam
          maxime dolorum fugit aut delectus, recusandae dolorem voluptatibus,
          suscipit nesciunt aliquid voluptas accusamus autem! Quia, voluptatem
          nemo. Adipisci, accusantium, ipsam quasi laboriosam nostrum magni
          nesciunt assumenda id saepe maiores itaque necessitatibus, tempore
          quibusdam quia iure et possimus autem at reprehenderit voluptatibus
          repellendus eaque dicta officiis perferendis? Eum! Laborum explicabo
          quidem impedit eligendi in ea ut esse inventore facilis. Id eveniet
          non reprehenderit in enim consectetur hic modi accusantium inventore
          nulla, temporibus dolorum, laudantium cumque! Numquam, minus fugiat.
          Voluptatibus veniam, sit suscipit quis sed sapiente molestias totam
          recusandae optio perspiciatis nihil velit, eius asperiores et maiores
          facilis ullam iste a, eveniet consequatur dolorem eos? Enim error
          blanditiis quas. Earum, similique dolor libero neque laboriosam
          perferendis exercitationem obcaecati placeat, magni ea, maxime
          corrupti eum! Laudantium libero placeat eos impedit beatae esse earum
          illo! Ex fugiat alias beatae iste praesentium. Ipsum, commodi
          inventore. Voluptate, praesentium eos repellendus at unde, cumque
          doloribus dolorum deserunt temporibus ipsam aliquam beatae molestias
          expedita assumenda iste delectus perspiciatis repudiandae consequatur
          vel porro soluta accusantium ducimus! Beatae magni, unde minima sit in
          fugiat? Consequuntur dolorum cumque rem est officiis! Nulla obcaecati
          praesentium rerum accusamus, saepe expedita velit, dolorem incidunt
          numquam nihil sit, perferendis omnis cupiditate cum. Repellat facilis
          nisi, iusto aut, sed officiis placeat fugiat modi incidunt recusandae
          numquam et rerum quis, hic est unde accusamus? Enim obcaecati
          molestiae officia aspernatur sapiente atque iste, illo minima? Dolor
          possimus tenetur natus veritatis numquam libero, fuga repellat
          expedita laudantium dolorum nobis voluptate, facilis quae perferendis,
          esse ipsa dignissimos deleniti. Reprehenderit totam incidunt libero
          deleniti doloremque, fugit ea excepturi. Porro architecto, tempore
          aliquid tempora eos eaque itaque voluptas temporibus sint! Officiis
          soluta blanditiis, perspiciatis dolorum veritatis, harum repellendus
          eveniet deleniti rem unde quaerat atque earum numquam quis velit
          dolore? Illum, eligendi distinctio consequuntur reprehenderit sapiente
          ipsam ab est magni veniam, nostrum quis ullam delectus adipisci
          laudantium neque animi consequatur inventore vitae? Dolor eveniet
          fugit nemo velit. Repellendus, omnis obcaecati? Architecto tenetur
          quas enim culpa vel odit natus consequatur velit nisi soluta. Eligendi
          soluta alias optio non eos ipsa repellat tenetur veniam ab ipsam vero
          itaque delectus aliquam, ratione odit. Voluptate fuga, vel commodi
          tempore voluptas natus quia neque, suscipit numquam in repellat maxime
          illum rerum inventore quibusdam nulla ut libero a dignissimos facilis
          expedita praesentium error culpa reiciendis? Modi? Culpa, distinctio!
          Ullam in molestias mollitia odio nihil ad ea quibusdam porro a quo
          facere illum, sit asperiores, cumque ipsam modi aspernatur nobis
          aperiam? Cum maiores optio alias autem placeat? Sit sed, enim
          dignissimos nobis asperiores omnis repudiandae in saepe provident
          praesentium! Ipsa eveniet, eum, labore quia architecto incidunt itaque
          nulla modi iusto similique ea magni pariatur beatae odit
          reprehenderit. Vitae earum ad, accusamus unde architecto illo? Nisi
          vero, sapiente eaque doloribus quisquam eum impedit quod doloremque
          praesentium nulla quae placeat veritatis accusantium molestiae
          dignissimos eius esse, voluptates corporis non! Eveniet ex dolore
          cumque voluptatibus accusantium architecto fuga consequatur quidem
          modi id pariatur fugit, minus nam, nobis reiciendis voluptas ea.
          Ratione tempora nesciunt pariatur nulla similique quisquam ut ducimus
          neque! Modi perferendis, eum sunt veniam sit sequi possimus
          praesentium cumque facilis voluptatibus, deserunt nostrum blanditiis
          ab ipsa, dolore deleniti! Eaque nam autem quo earum enim repudiandae
          laudantium, minus amet pariatur. Ullam modi necessitatibus nesciunt
          accusantium. Sint ipsam recusandae rem voluptatibus ex excepturi. Sed
          enim voluptas fuga nulla quos officiis eaque perspiciatis pariatur
          corporis cumque ipsum, deleniti possimus harum dolorem dolores!
          Aspernatur, a? Blanditiis illo sit earum dolor sed hic neque beatae?
          Soluta excepturi cumque molestias, iure suscipit, quisquam atque eaque
          omnis natus earum hic ducimus facere architecto perferendis labore
          praesentium. Sit voluptatibus, debitis sequi velit quam dolore quos
          recusandae voluptatem impedit? Laboriosam officiis labore consequatur?
          Obcaecati aperiam, quas, qui, tempora neque voluptas at provident
          quisquam unde dolorum possimus omnis beatae? Nesciunt, saepe
          accusantium. Nisi dicta voluptates exercitationem laborum saepe nam
          voluptatibus blanditiis sapiente quas quod beatae sint culpa fugit
          itaque, minima ipsa commodi. Nisi distinctio placeat pariatur, ducimus
          mollitia omnis. Officiis, eum qui a commodi ab magni perferendis
          assumenda quasi ipsa. Molestiae tempore consequatur dolor rem
          voluptatibus quasi dolore pariatur facilis magni, culpa, beatae
          repudiandae harum, voluptate quae expedita non? Iusto tempore nulla
          doloribus officia veritatis ipsum nihil velit accusamus reprehenderit
          iste quasi, earum architecto officiis, nisi, totam delectus fugit
          voluptatibus laborum doloremque quos est odio! Nostrum aspernatur
          velit ab. Consequatur asperiores aliquam fugiat blanditiis quis hic
          aspernatur natus laboriosam veritatis perferendis maiores, harum
          quaerat autem culpa illum. Quae a necessitatibus accusantium nemo,
          maiores id facilis iusto optio commodi laborum! Qui officia nam
          pariatur facere, quos dolore eveniet nobis veritatis optio fuga ex
          ipsam commodi dolorem accusamus consectetur fugit maiores totam
          similique magni harum repellat laudantium labore! Quidem, cum vero.
          Perferendis maxime dignissimos aliquid debitis molestiae magnam quae
          cupiditate, nesciunt earum, fugit magni provident explicabo id
          voluptates minus a velit officiis! Illo voluptates ducimus voluptatem
          vero iusto vitae deleniti. Incidunt! Itaque veritatis rerum omnis quod
          dolore unde est provident, officiis laboriosam explicabo sapiente ipsa
          dolorem, vero nemo debitis deserunt similique, atque quidem iusto
          consequuntur! Dolores ratione at quaerat id molestias. Itaque suscipit
          aut fugit iusto voluptas eum aperiam animi maiores rem, veritatis
          provident consequatur id laboriosam, ipsa aspernatur delectus?
          Blanditiis, qui sapiente cumque dignissimos minus enim ducimus!
          Consequatur, aspernatur labore! Sint odio molestiae est eius ratione,
          dignissimos sequi minima? Debitis cupiditate ratione repellat vel quos
          odio deserunt eos quae earum, pariatur aliquam magnam minus, illum
          dolor laborum quis maiores dolore?
        </div>
      </div>
    </div>
  </main>
  <PageFooter />
</template>

<style scoped lang="scss">
main {
  .intro {
    padding-top: 5.75rem;
    padding-bottom: 8.69rem;

    h1 {
      margin-top: 0;
      margin-bottom: 2.875rem;

      .title-logo {
        width: 100%;
        max-width: 960px;
        margin-inline: auto;
      }
    }

    .narrow {
      margin-inline: auto;
      max-width: 550px;

      .description {
        font-size: 1.5rem;
        font-weight: 500;

        :deep(a) {
          font-weight: 600;
          color: #092bba;
        }
      }

      .button {
        margin-top: 2.875rem;
        margin-inline: auto;
        max-width: 404px;
      }
    }
  }

  .explanations {
    padding-top: 7.4375rem;
    padding-bottom: 8.8125rem;

    h2 {
      margin-top: 0;
      margin-bottom: 2.5rem;
      font-size: 2.25rem;
      font-weight: 700;
      text-align: center;
    }

    .content {
      padding: 2.1875rem 2.9375rem 2.5625rem 3.8125rem;
      // background-image: url.svg($bg-svg-string);
      background-color: var(--manipulacija-color-8);
      background-repeat: no-repeat;
      background-size: 100% 100%;
    }
  }
}
</style>
