---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

## Presentaties i&i conferentie

Deze website bevat de presentaties van de i&i conferentie van 7 en 8 november 2018.

(Nog niet alle presentaties zijn beschikbaar.
We proberen deze zo spoedig mogelijk toe te voegen.)

## Examenprogramma informatica

Het nieuwe examenprogramma voor het HAVO/VWO-vak informatica gaat in per september 2019.
Momenteel wordt er hard gewerkt aan het ontwikkelen van lesmateriaal hiervoor.
De verschillende methodes zorgen voor het materiaal voor het verplichte deel van het programma.
In opdracht van SLO werken de informatica-steunpunten samen met docententeams aan het materiaal voor de keuzethema's.

* [Algoritmiek]({{ site.baseurl }}/themas/algoritmiek.html)
* [Databases]({{ site.baseurl }}/themas/databases.html)
* [Game design]({{ site.baseurl }}/themas/gamedesign.html)
* [Netwerken-Internet of Things]({{ site.baseurl}}/themas/netwerken.html)
* [Physical computing]({{ site.baseurl }}/themas/physical-computing)
* [Computational Science: Agent based modeling]({{ site.baseurl }}/themas/computational-science)


## Nieuws

<div>
{%- if site.posts.size > 0 -%}
  <ul class="post-list">
    {%- for post in site.posts -%}
    <li>
      <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.title | escape }}
      </a>
      {%- assign date_format = site.minima.date_format | default: "%-d-%b-%Y" -%}
      <span class="post-meta">({{ post.date | date: date_format }})</span>
      {%- if site.show_excerpts -%}
        {{ post.excerpt }}
      {%- endif -%}
    </li>
    {%- endfor -%}
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | relative_url }}">via RSS</a></p>
{%- endif -%}
</div>

## Agenda

<div class="agenda-list">
  <ul>
    {% for post in site.categories["agenda"] %}
      <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.agendadate}} - {{post.title}}</a></h4>
    {% endfor %}
  </ul>
</div>
