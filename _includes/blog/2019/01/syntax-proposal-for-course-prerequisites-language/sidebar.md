{% capture nav-bar %}
{% assign and-keyword = '<span class="ow">AND</span>' %}
{% assign or-keyword = '<span class="ow">OR</span>' %}
{% assign not-keyword = '<span class="ow">NOT</span>' %}
{% assign inline-and = and-keyword | prepend: '<code>' | append: '</code>' %}
{% assign inline-or = or-keyword | prepend: '<code>' | append: '</code>' %}
{% assign inline-not = not-keyword | prepend: '<code>' | append: '</code>' %}
* [back to top](#)
* [1. Variables](#sec-1)
  - [1.1 Whitespace](#sec-1-1)
  - [1.2 Term: "Name"](#sec-1-2)
  - [1.3 Whitespace](#sec-1-3)
  - [1.4 Whitespace](#sec-1-4)
* [2. Punctuation](#sec-2)
  - [2.1 Sentences](#sec-2-1)
  - [2.2 Paragraphs](#sec-2-2)
  - [2.3 Double Newline](#sec-2-3)
  - [2.4 Last Sentence](#sec-2-4)
  - [2.5 Outer Whitespace](#sec-2-5)
  - [2.6 Comments](#sec-2-6)
* [3. Keywords](#sec-3)
  - [3.1 Boolean Operators](#sec-3-1)
  - [3.2 Potential Problems](#sec-3-2)
  - [3.3 Uppercase Keywords](#sec-3-3)
  - [3.4 Escaping](#sec-3-4)
  - [3.5 Context-Based Syntax](#sec-3-5)
* [4. Object Types](#sec-4)
  - [4.1 Term: "List"](#sec-4-1)
  - [4.2 List Syntax](#sec-4-2)
  - [4.3 Name Typing](#sec-4-3)
* [5. Quantifiers](#sec-5)
  - [5.1 Notation](#sec-5-1)
  - [5.2 Implicit Quantifier](#sec-5-2)
  - [5.3 Special Cases](#sec-5-3)
  - [5.4 Implicit Truth Value](#sec-5-4)
  - [5.5 Explicit Conversion](#sec-5-5)
* [6. List Operations Cont.](#sec-6)
  - [6.1 Combining Lists](#sec-6-1)
  - [6.2 Comparing Lists](#sec-6-2)
  - [6.3 {{ inline-and }} Implicit Behavior](#sec-6-3)
  - [6.4 {{ inline-or }} Implicit Behavior](#sec-6-4)
* [7. Miscellaneous](#sec-7)
  - [7.1 Reading Files](#sec-7-1)
  - [7.2 SQL for Meta Files](#sec-7-2)
  - [7.3 Name Resolution](#sec-7-3)
  - [7.4 Printing the Last Line](#sec-7-4)
  - [7.5 Title Comments](#sec-7-5)
  - [7.6 Degree Requirements](#sec-7-6)

{% endcapture %}
<style>
#left-navbar {
  position: sticky;
  top: 10px;
  background: white;
  border-radius: 10px;
  margin-top: 5px;
  margin-bottom: 5px;
  padding-left: 10px;
}
#left-navbar ul {
  padding-left: 10px;
}
</style>

<!-- https://stackoverflow.com/questions/28452235/make-a-nav-bar-stick-to-the-top-when-scrolling-with-css -->
<div id="left-navbar">
<small>{{ nav-bar | strip | markdownify }}</small>
</div>

<script>
function setNavbarScroll() {
  var navbar = document.getElementById('left-navbar');
  if (window.innerWidth > 992) {
    navbar.style.height = (window.innerHeight - 20).toString()+"px";
    navbar.style.overflow = "scroll auto";
  } else {
    navbar.style.height = "auto";
    navbar.style.overflow = "auto";
  }
}
setNavbarScroll();
var resizeId;
window.addEventListener("resize", function() {
  clearTimeout(resizeId);
  resizeId = setTimeout(setNavbarScroll, 250);
});
</script>
