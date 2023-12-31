{% if matches.has_other_pages %}


<!-- ***** Displays Previous***** -->
    {% if matches.has_previous %}
        <a  href="?page={{ matches.previous_page_number }}">&laquo; </a>
    {% else %}
        <a class="bg-secondary text-dark">&laquo; </a>
    {% endif %}
<!-- ***** Displays Previous ***** -->


<!-- ***** Displays first character ***** -->
    {% if matches.number == 1 %}
       <a  class="bg-warning text-light">{{ matches.number }}</a>
    {% else %}
     <a href='?page={{ 1 }}'>{{ 1 }}</a>
    {% endif %}
<!-- ***** Displays first character ends ***** -->


<!-- ***** Displays if paging already greater than 2 ***** -->
    {% if matches.number > 2 %}
      <a  class="bg-danger text-light">..</a>
    {% endif %}
<!-- ***** Displays if paging already greater than 2 ***** -->


<!-- ***** Displays each page ***** -->
    {% for page_num in matches.paginator.page_range %}
    {% if matches.number == page_num and matches.number != matches.paginator.num_pages and  matches.number != 1%}
      <a  class="bg-warning text-light">{{ page_num }}</a>
    {% endif %}
    {% endfor %}
<!-- ***** Displays each page ***** -->


<!-- ***** Displays if paging already close to the last one ***** -->
    {% if matches.number < matches.paginator.num_pages|add:"-1" %}
       <a  class="bg-primary text-light">..</a>
    {% endif %}
<!-- ***** Displays if paging already close to the last one ***** -->


<!-- ***** Displays the last number ***** -->
    {% if matches.number == matches.paginator.num_pages %}
       <a  class="bg-warning text-light">{{ matches.number }}</a>
    {% else %}
        <a href='?page={{ matches.paginator.num_pages }}'>{{ matches.paginator.num_pages }}</a>
    {% endif %}
<!-- ***** Displays the last number ***** -->


<!-- ***** Displays Next ***** -->
    {% if matches.has_next %}
        <a  href="?page={{ matches.next_page_number }}">&raquo; </a>
    {% else %}
        <a  class="bg-secondary text-light btn-disabled">&raquo; </a>
    {% endif %}
<!-- ***** Displays Next ***** -->



{% endif %}
