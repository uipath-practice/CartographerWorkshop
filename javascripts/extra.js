document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('a[href^="http"]').forEach(function (link) {
    if (!link.href.startsWith(window.location.origin)) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
    }
  });
});

// Collapsible top-level sections.
// Opt in per page by placing <div class="collapsible-sections" hidden></div> in the markdown.
// Each h2 becomes a toggle for everything up to the next h2. Sections start expanded,
// headings stay in the table of contents, and jumping to an anchor opens its section.
document.addEventListener('DOMContentLoaded', function () {
  var article = document.querySelector('.md-content__inner');
  if (!article || !article.querySelector('.collapsible-sections')) return;

  var refreshScrollSpy = function () {
    window.dispatchEvent(new Event('resize'));
  };

  var setCollapsed = function (heading, body, collapsed) {
    heading.classList.toggle('is-collapsed', collapsed);
    body.classList.toggle('is-collapsed', collapsed);
    heading.setAttribute('aria-expanded', String(!collapsed));
  };

  var sections = [];
  article.querySelectorAll(':scope > h2').forEach(function (heading) {
    var body = document.createElement('div');
    body.className = 'section-body';
    var node = heading.nextSibling;
    while (node && !(node.nodeType === 1 && /^(H2|ASIDE|FOOTER)$/.test(node.tagName))) {
      var next = node.nextSibling;
      body.appendChild(node);
      node = next;
    }
    heading.after(body);
    heading.classList.add('section-toggle');
    heading.setAttribute('role', 'button');
    heading.setAttribute('tabindex', '0');
    heading.setAttribute('aria-expanded', 'true');
    sections.push({ heading: heading, body: body });

    var toggle = function (event) {
      if (event.target.closest('.headerlink')) return;
      setCollapsed(heading, body, !heading.classList.contains('is-collapsed'));
      refreshScrollSpy();
    };
    heading.addEventListener('click', toggle);
    heading.addEventListener('keydown', function (event) {
      if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); toggle(event); }
    });
  });

  var revealHash = function () {
    if (!location.hash) return;
    var target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (!target) return;
    sections.forEach(function (s) {
      if (s.body.contains(target) && s.heading.classList.contains('is-collapsed')) {
        setCollapsed(s.heading, s.body, false);
        refreshScrollSpy();
      }
    });
    target.scrollIntoView();
  };
  window.addEventListener('hashchange', revealHash);
  revealHash();
});

// Collapsible main sections in the left-hand table of contents.
// Every top-level TOC entry that has sub-steps gets a chevron that shows or hides them.
// Entries start expanded; following a link to a hidden step expands its entry again.
document.addEventListener('DOMContentLoaded', function () {
  var toc = document.querySelector('.md-sidebar--primary .md-nav--secondary');
  if (!toc) return;

  var groups = [];
  toc.querySelectorAll(':scope > .md-nav__list > .md-nav__item').forEach(function (item) {
    var children = item.querySelector(':scope > nav.md-nav');
    var link = item.querySelector(':scope > a.md-nav__link');
    if (!children || !link) return;

    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'toc-toggle';
    button.setAttribute('aria-expanded', 'true');
    button.setAttribute('aria-label', 'Collapse ' + link.textContent.trim());
    item.classList.add('toc-group');
    item.insertBefore(button, link);
    groups.push({ item: item, button: button, label: link.textContent.trim() });

    button.addEventListener('click', function (event) {
      event.preventDefault();
      event.stopPropagation();
      var collapsed = item.classList.toggle('toc-collapsed');
      button.setAttribute('aria-expanded', String(!collapsed));
      button.setAttribute('aria-label', (collapsed ? 'Expand ' : 'Collapse ') + link.textContent.trim());
    });
  });

  var expandForHash = function () {
    if (!location.hash) return;
    groups.forEach(function (g) {
      var hit = g.item.querySelector('a.md-nav__link[href="' + location.hash + '"]');
      if (hit && g.item.classList.contains('toc-collapsed')) {
        g.item.classList.remove('toc-collapsed');
        g.button.setAttribute('aria-expanded', 'true');
        g.button.setAttribute('aria-label', 'Collapse ' + g.label);
      }
    });
  };
  window.addEventListener('hashchange', expandForHash);
  expandForHash();
});
