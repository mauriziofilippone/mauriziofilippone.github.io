(function () {
  // Fetch the research page and pick today's paper by day-of-year % N.
  // No hardcoded list: adding a paper to research.md automatically
  // enters it into the rotation on the next site build.
  fetch('/research/')
    .then(function (r) { return r.text(); })
    .then(function (html) {
      var doc = new DOMParser().parseFromString(html, 'text/html');

      // Walk the research page collecting section context and entries in order
      var nodes = doc.querySelectorAll('h2.research-section, .research-entry');
      var papers = [];
      var currentSectionId   = '';
      var currentSectionName = '';

      nodes.forEach(function (el) {
        if (el.tagName === 'H2') {
          currentSectionId   = el.id;
          currentSectionName = el.textContent.trim();
        } else {
          var img      = el.querySelector('img');
          var h3       = el.querySelector('h3');
          var ps       = el.querySelectorAll('p');
          // first research-links anchor whose text is "Paper"
          var linkEl   = el.querySelector('.research-links a');
          // skip the up-Section / up-Top anchors
          el.querySelectorAll('.research-links a').forEach(function (a) {
            if (a.textContent.trim() === 'Paper') linkEl = a;
          });
          if (!h3) return; // skip malformed entries
          var descText = ps.length > 1 ? ps[1].textContent.trim() : '';
          if (descText.length > 310) descText = descText.slice(0, 310) + '…';
          papers.push({
            img  : img    ? img.getAttribute('src')  : '',
            title: h3.textContent.trim(),
            cite : ps.length > 0 ? ps[0].textContent.trim() : '',
            desc : descText,
            link : linkEl  ? linkEl.getAttribute('href') : '#',
            sid  : currentSectionId,
            sn   : currentSectionName
          });
        }
      });

      if (!papers.length) {
        document.getElementById('highlight-card').innerHTML =
          '<div class="highlight-body"><p style="opacity:0.4;font-size:0.9rem">' +
          'Highlight unavailable (nodes: ' + nodes.length + ').</p></div>';
        return;
      }

      // Deterministic daily pick: day-of-year % N
      var now   = new Date();
      var start = new Date(now.getFullYear(), 0, 0);
      var doy   = Math.floor((now - start) / 864e5); // 1-366
      var p     = papers[doy % papers.length];

      document.getElementById('highlight-label').textContent =
        'Highlight of the day · day ' + doy + ' of ' + now.getFullYear();

      var paperLink = (p.link && p.link !== '#')
        ? '<a href="' + p.link + '" target="_blank" rel="noopener">Paper ↗</a>'
        : '';
      var sectionLink = '<a href="/research/#' + p.sid + '">More on ' + p.sn + ' →</a>';

      document.getElementById('highlight-card').innerHTML =
        '<div class="highlight-thumb">' +
          '<img src="' + p.img + '" alt="">' +
        '</div>' +
        '<div class="highlight-body">' +
          '<a class="highlight-badge" href="/research/#' + p.sid + '">' + p.sn + '</a>' +
          '<p class="highlight-title">' + p.title + '</p>' +
          '<p class="highlight-citation">' + p.cite + '</p>' +
          '<p class="highlight-desc">' + p.desc + '</p>' +
          '<div class="highlight-links">' + paperLink + sectionLink + '</div>' +
        '</div>';
    })
    .catch(function () {
      document.getElementById('highlight-card').innerHTML =
        '<div class="highlight-body"><p style="opacity:0.4;font-size:0.9rem">Highlight unavailable.</p></div>';
    });
})();
