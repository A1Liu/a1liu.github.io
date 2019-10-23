{% capture nav_bar %}
[Home]({{ site.baseurl }}/)
[Blog]({{ site.baseurl }}/blog)
[Career]({{ site.baseurl }}/career)
[Resources]({{ site.baseurl }}/resources)
{% endcapture %}
{{ nav_bar | markdownify }}
