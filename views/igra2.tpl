% import model
% rebase('UVP\\Vislice\\views\\base.tpl', title="Vislice")  # title parameter zgleda nč ne nardi. Mogoče nadomestek, če slučajn naslova ni. Lah napišeš karkol v title
<!-- id_igre, igra, in poskus se prenesejo sem  --->

<table>
    <tr>
      <td>
        <h2>{{igra.pravilni_del_gesla()}}</h2>
      </td>
    </tr>
    <tr>
      <td>
        Nepravilni ugibi : {{igra.nepravilni_ugibi()}}
      </td>
    </tr>
    <tr>
      <td>
      <img src="../img/{{igra.stevilo_napak()}}.jpg" alt="obesenec">  <!-- tu smo odstranili (glede na igra1) ../ -->
        Stopnja obešenosti : {{igra.stevilo_napak()}} / {{model.STEVILO_DOVOLJENIH_NAPAK + 1}}  <!-- slash ni deljenje tukaj --->
      </td>
    </tr>
  </table>

  % if poskus == model.ZMAGA:

  <h1>ZMAGA!</h1>
  <form action="/nova_igra/" method="post">  <!-- tu je prej bil sam igra --->
    <button type="submit">Nova igra</button>
  </form>

  % elif poskus == model.PORAZ:

  <h1> LOSER! </h1>

  Pravilno geslo: {{igra.geslo}}

  <form action="/nova_igra/" method="post">  <!-- tu je prej bil sam igra --->
    <button type="submit">Nova igra</button>
  </form>

  % else:

  <form action="/igra/" method="post">  <!-- tu je prej bil id igre -->
    Črka: <input type="text" name='crka' autofocus>
    <button type="submit">Pošlji ugib</button>
  </form>

  % end