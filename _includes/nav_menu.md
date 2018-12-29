{% capture nav_bar %}
* [Home]({{ site.baseurl }}/)
* [Posts]({{ site.baseurl }}/posts)
* [Bored]({{ site.baseurl }}/bored)
* [Resources]({{ site.baseurl }}/resources)
{% endcapture %}
{{ nav_bar | markdownify }}
