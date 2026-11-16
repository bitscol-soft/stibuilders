/* STI Builders — interactions. Vanilla JS, no dependencies. */
(function () {
  'use strict';

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const on = (el, ev, fn, opts) => el && el.addEventListener(ev, fn, opts);

  /* ---------- header state ---------- */
  const header = $('#siteHeader');
  const heroNav = document.body.classList.contains('has-hero');

  function syncHeader() {
    if (!header) return;
    header.classList.toggle('is-solid', window.scrollY > 40 || !heroNav);
  }

  syncHeader();
  on(window, 'scroll', syncHeader, { passive: true });

  /* ---------- mobile drawers ---------- */
  const drawer = $('#drawer');
  const openDrawer = () => { drawer.classList.add('is-open'); drawer.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden'; };
  const closeDrawer = () => { drawer.classList.remove('is-open'); drawer.setAttribute('aria-hidden', 'true'); document.body.style.overflow = ''; };
  on($('#drawerOpen'), 'click', openDrawer);
  $$('[data-close-drawer]').forEach(b => on(b, 'click', closeDrawer));

  const overlay = $('#searchOverlay');
  const openSearch = () => { overlay.classList.add('is-open'); setTimeout(() => $('input[type=search]', overlay)?.focus(), 60); };
  const closeSearch = () => overlay.classList.remove('is-open');
  on($('#searchOpen'), 'click', openSearch);
  $$('[data-close-search]').forEach(b => on(b, 'click', closeSearch));
  on(overlay, 'click', e => { if (e.target === overlay) closeSearch(); });
  on(document, 'keydown', e => {
    if (e.key === 'Escape') { closeSearch(); closeDrawer(); closeLightbox(); $('.filter-side')?.classList.remove('is-open'); }
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
      e.preventDefault(); openSearch();
    }
  });

  /* ---------- reveal on scroll ---------- */
  const io = 'IntersectionObserver' in window ? new IntersectionObserver((entries) => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 }) : null;
  $$('[data-reveal]').forEach((el, i) => {
    el.style.transitionDelay = (Math.min(i % 6, 5) * 60) + 'ms';
    if (io) io.observe(el); else el.classList.add('is-in');
  });

  /* ---------- counters ---------- */
  const counters = $$('[data-count]');
  if (counters.length) {
    const cObs = 'IntersectionObserver' in window ? new IntersectionObserver((entries) => {
      entries.forEach(en => {
        if (!en.isIntersecting) return;
        const el = en.target;
        const target = parseFloat(el.dataset.count || '0');
        const dur = 1400;
        const start = performance.now();
        const fmt = (v) => el.dataset.format === 'comma' ? Math.round(v).toLocaleString('en-IN') : Math.round(v);
        const step = (now) => {
          const p = Math.min((now - start) / dur, 1);
          const eased = 1 - Math.pow(1 - p, 3);
          el.textContent = fmt(target * eased);
          if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
        cObs.unobserve(el);
      });
    }, { threshold: 0.4 }) : null;
    counters.forEach(c => { if (cObs) cObs.observe(c); else c.textContent = c.dataset.count; });
  }

  /* ---------- save (favourite) ---------- */
  function csrf() {
    const m = document.cookie.match(/csrftoken=([^;]+)/);
    return m ? m[1] : '';
  }
  $$('[data-save]').forEach(btn => {
    on(btn, 'click', async (e) => {
      e.preventDefault();
      e.stopPropagation();
      const slug = btn.dataset.save;
      try {
        const res = await fetch('/saved/toggle/', {
          method: 'POST',
          headers: { 'X-CSRFToken': csrf(), 'Content-Type': 'application/x-www-form-urlencoded', 'X-Requested-With': 'XMLHttpRequest' },
          body: 'slug=' + encodeURIComponent(slug),
        });
        const data = await res.json();
        btn.classList.toggle('is-on', data.saved);
        btn.setAttribute('aria-pressed', data.saved ? 'true' : 'false');
        const use = btn.querySelector('use');
        if (use) use.setAttribute('href', data.saved ? '#i-heart-fill' : '#i-heart');
        const badge = $('#savedCount');
        if (badge) { badge.textContent = data.count; badge.hidden = data.count === 0; }
      } catch (err) { /* offline: ignore */ }
    });
  });

  /* ---------- hero carousel ---------- */
  const heroSlides = $$('[data-hero-slide]');
  if (heroSlides.length > 1) {
    const dots = $$('[data-hero-dot]');
    let idx = 0, timer;
    const show = (i) => {
      idx = (i + heroSlides.length) % heroSlides.length;
      heroSlides.forEach((s, k) => { s.style.opacity = k === idx ? 1 : 0; s.style.zIndex = k === idx ? 1 : 0; });
      dots.forEach((d, k) => d.classList.toggle('is-active', k === idx));
    };
    heroSlides.forEach((s, i) => { s.style.transition = 'opacity 1.1s ease'; s.style.position = 'absolute'; s.style.inset = '0'; if (i) s.style.opacity = 0; });
    dots.forEach((d, i) => on(d, 'click', () => { show(i); restart(); }));
    const restart = () => { clearInterval(timer); timer = setInterval(() => show(idx + 1), 7000); };
    show(0); restart();
  }

  /* ---------- accordions ---------- */
  $$('.acc__head').forEach(head => {
    on(head, 'click', () => {
      const item = head.closest('.acc__item');
      const open = item.classList.contains('is-open');
      const group = head.closest('.acc');
      if (group && group.dataset.single !== 'false') $$('.acc__item', group).forEach(i => i.classList.remove('is-open'));
      item.classList.toggle('is-open', !open);
      head.setAttribute('aria-expanded', String(!open));
    });
  });

  /* ---------- filter groups collapse ---------- */
  $$('.fgroup__head').forEach(h => on(h, 'click', () => h.closest('.fgroup').classList.toggle('is-collapsed')));

  /* ---------- filter side drawer (mobile) ---------- */
  on($('#filterOpen'), 'click', () => $('.filter-side')?.classList.add('is-open'));
  on($('#filterClose'), 'click', () => $('.filter-side')?.classList.remove('is-open'));

  /* ---------- auto-submit filter form (debounced) ---------- */
  const filterForm = $('#filterForm');
  if (filterForm) {
    let t;
    const submit = () => { clearTimeout(t); t = setTimeout(() => filterForm.submit(), 380); };
    $$('input[type=checkbox], input[type=radio], select', filterForm).forEach(el => on(el, 'change', () => filterForm.submit()));
    $$('input[type=number], input[type=range]', filterForm).forEach(el => on(el, 'input', submit));
  }

  /* ---------- view switch (grid / list) ---------- */
  const resultsGrid = $('#resultsGrid');
  $$('[data-view]').forEach(btn => on(btn, 'click', () => {
    $$('[data-view]').forEach(b => b.classList.remove('is-active'));
    btn.classList.add('is-active');
    const mode = btn.dataset.view;
    if (resultsGrid) resultsGrid.classList.toggle('is-list', mode === 'list');
  }));

  /* ---------- tabs ---------- */
  $$('[data-tabs]').forEach(group => {
    const buttons = $$('[data-tab]', group);
    buttons.forEach(btn => on(btn, 'click', () => {
      buttons.forEach(b => b.classList.remove('is-active'));
      btn.classList.add('is-active');
      const target = btn.dataset.tab;
      const scope = group.dataset.tabs;
      $$(`[data-pane]`, document).forEach(p => {
        if (p.dataset.pane && p.closest('[data-tab-scope]')?.dataset.tabScope === scope) {
          p.hidden = p.dataset.pane !== target;
        }
      });
      $$(`[data-gallery-filter]`).forEach(a => {
        if (a.dataset.galleryFilter !== undefined && scope === 'gallery') a.hidden = false;
      });
    }));
  });

  /* ---------- project detail subnav scroll spy ---------- */
  const subLinks = $$('.pd-subnav a[href^="#"]');
  if (subLinks.length) {
    const sections = subLinks.map(a => document.getElementById(a.getAttribute('href').slice(1))).filter(Boolean);
    const spy = () => {
      let active = sections[0];
      sections.forEach(sec => { if (sec.getBoundingClientRect().top <= 140) active = sec; });
      subLinks.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#' + active.id));
    };
    on(window, 'scroll', spy, { passive: true });
    spy();
  }

  /* ---------- lightbox ---------- */
  let lbIndex = 0, lbItems = [];
  const lb = $('#lightbox');
  function closeLightbox() { if (lb) { lb.classList.remove('is-open'); document.body.style.overflow = ''; } }
  window.closeLightbox = closeLightbox;
  function openLightbox(items, index) {
    if (!lb) return;
    lbItems = items; lbIndex = index;
    renderLightbox();
    lb.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }
  function renderLightbox() {
    if (!lb) return;
    const item = lbItems[lbIndex];
    if (!item) return;
    const img = $('#lightboxImg');
    img.src = item.src; img.alt = item.caption || '';
    $('#lightboxCaption').textContent = (item.caption || '') + `  ·  ${lbIndex + 1}/${lbItems.length}`;
  }
  $$('[data-lightbox]').forEach(a => on(a, 'click', (e) => {
    e.preventDefault();
    const group = a.dataset.lightbox || 'default';
    const items = $$(`[data-lightbox="${group}"]`).map(x => ({ src: x.getAttribute('href'), caption: x.dataset.caption || '' }));
    openLightbox(items, items.findIndex(x => x.src === a.getAttribute('href')));
  }));
  on($('#lightboxClose'), 'click', closeLightbox);
  on($('#lightboxPrev'), 'click', () => { lbIndex = (lbIndex - 1 + lbItems.length) % lbItems.length; renderLightbox(); });
  on($('#lightboxNext'), 'click', () => { lbIndex = (lbIndex + 1) % lbItems.length; renderLightbox(); });
  on(lb, 'click', e => { if (e.target === lb) closeLightbox(); });
  on(document, 'keydown', e => {
    if (!lb || !lb.classList.contains('is-open')) return;
    if (e.key === 'ArrowRight') { lbIndex = (lbIndex + 1) % lbItems.length; renderLightbox(); }
    if (e.key === 'ArrowLeft') { lbIndex = (lbIndex - 1 + lbItems.length) % lbItems.length; renderLightbox(); }
  });

  /* ---------- share ---------- */
  $$('[data-share]').forEach(btn => on(btn, 'click', async () => {
    const url = btn.dataset.url || location.href;
    const title = btn.dataset.title || document.title;
    const net = btn.dataset.share;
    if (net === 'native') {
      if (navigator.share) { try { await navigator.share({ title, url }); } catch (e) {} }
      else copy(url, btn);
      return;
    }
    const map = {
      facebook: `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`,
      twitter: `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(title)}`,
      linkedin: `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`,
      whatsapp: `https://wa.me/?text=${encodeURIComponent(title + ' ' + url)}`,
      pinterest: `https://pinterest.com/pin/create/button/?url=${encodeURIComponent(url)}&description=${encodeURIComponent(title)}`,
      email: `mailto:?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(url)}`,
    };
    if (net === 'copy') { copy(url, btn); return; }
    if (map[net]) window.open(map[net], '_blank', 'noopener,width=680,height=640');
  }));
  function copy(text, btn) {
    const done = () => {
      const old = btn.innerHTML;
      btn.innerHTML = '<svg class="ico"><use href="#i-check"></use></svg>';
      setTimeout(() => { btn.innerHTML = old; }, 1600);
    };
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done);
    else { const t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select(); document.execCommand('copy'); t.remove(); done(); }
  }

  /* ---------- back to top ---------- */
  const toTop = $('#toTop');
  on(window, 'scroll', () => toTop?.classList.toggle('is-on', window.scrollY > 700), { passive: true });
  on(toTop, 'click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ---------- booking wizard ---------- */
  const bookingForm = $('#bookingForm');
  if (bookingForm) {
    const steps = $$('[data-step]', bookingForm);
    const panes = $$('[data-pane]', bookingForm);
    let step = 0;
    const showStep = (i) => {
      step = Math.max(0, Math.min(i, panes.length - 1));
      panes.forEach((p, k) => p.hidden = k !== step);
      $$('.step', bookingForm).forEach((s, k) => {
        s.classList.toggle('is-active', k === step);
        s.classList.toggle('is-done', k < step);
      });
      const sum = $('#bookingSummary');
      if (sum && step === panes.length - 1) sum.hidden = false;
      syncSummary();
    };
    function syncSummary() {
      const projectSel = $('select[name=project]', bookingForm);
      const unitSel = $('select[name=apartment]', bookingForm);
      const date = $('input[name=preferred_date]', bookingForm);
      const slot = $('input[name=preferred_time]:checked', bookingForm);
      const set = (id, val) => { const el = document.getElementById(id); if (el) el.textContent = val || '—'; };
      set('sumProject', projectSel?.selectedOptions[0]?.text);
      set('sumUnit', unitSel?.selectedOptions[0]?.text);
      set('sumDate', date?.value);
      set('sumTime', slot?.value);
    }
    const stepFields = (i) => $$('[data-required]', panes[i] || document.createElement('div'));
    const validateStep = (i) => {
      const err = $('#bkError');
      let ok = true;
      stepFields(i).forEach(f => {
        const valid = f.type === 'checkbox' ? f.checked : !!f.value.trim();
        f.style.borderColor = valid ? '' : '#b03030';
        if (!valid && ok) { ok = false; f.focus(); }
      });
      if (err) {
        err.hidden = ok;
        err.textContent = ok ? '' : 'Please complete your name, mobile number and consent to continue.';
      }
      return ok;
    };
    $$('[data-next]').forEach(b => on(b, 'click', () => {
      if (step === 1 && !validateStep(1)) return;
      if (err0) err0.hidden = true;
      showStep(step + 1);
    }));
    $$('[data-prev]').forEach(b => on(b, 'click', () => showStep(step - 1)));
    $$('input, select, textarea', bookingForm).forEach(el => on(el, 'change', syncSummary));
    const err0 = $('#bkError');
    on(bookingForm, 'submit', (e) => {
      if (!validateStep(1)) { e.preventDefault(); showStep(1); }
    });
    showStep(0);

    /* filter units when project changes */
    const projSel = $('select[name=project]', bookingForm);
    const unitSel = $('select[name=apartment]', bookingForm);
    if (projSel && unitSel) {
      const loadUnits = async () => {
        const slug = projSel.selectedOptions[0]?.dataset.slug;
        unitSel.innerHTML = '<option value="">Any available unit</option>';
        if (!slug) return;
        try {
          const res = await fetch(`/projects/${slug}/units.json`);
          const data = await res.json();
          data.units.filter(u => u.status === 'available').forEach(u => {
            const o = document.createElement('option');
            o.value = u.id;
            o.textContent = `${u.label} · ${u.size} sft · ${u.price}`;
            unitSel.appendChild(o);
          });
        } catch (e) {}
      };
      on(projSel, 'change', loadUnits);
    }
  }

  /* ---------- inventory rows ---------- */
  $$('[data-row-link]').forEach(row => on(row, 'click', (e) => {
    if (e.target.closest('a, button')) return;
    window.location.href = row.dataset.rowLink;
  }));

  /* ---------- copy buttons ---------- */
  $$('[data-copy]').forEach(btn => on(btn, 'click', () => copy(btn.dataset.copy, btn)));

  /* ---------- gallery lightbox groups on detail pages ---------- */
  $$('[data-plan-open]').forEach(btn => on(btn, 'click', () => {
    const items = $$('[data-plan-item]').map(x => ({ src: x.getAttribute('href'), caption: x.dataset.caption || '' }));
    const i = items.findIndex(x => x.src === btn.dataset.planOpen);
    openLightbox(items, i < 0 ? 0 : i);
  }));

  /* ---------- map rendering (no external libs) ---------- */
  const mapEl = $('#projectsMap');
  if (mapEl && window.__mapPoints) {
    renderMap(mapEl, window.__mapPoints);
  }
  function renderMap(root, points) {
    const project = (lat, lng) => {
      const latR = 0.055, lngR = 0.085;
      const x = ((lng + 90.42) / lngR) * 100;
      const y = ((23.95 - lat) / latR) * 100;
      return { x: Math.max(3, Math.min(97, x)), y: Math.max(2, Math.min(96, y)) };
    };
    root.innerHTML = '';
    const inner = document.createElement('div');
    inner.className = 'map-canvas';
    points.forEach(p => {
      const pos = project(p.lat || 23.8759, p.lng || 90.3795);
      const a = document.createElement('a');
      a.className = 'map-marker';
      a.href = p.url || '#';
      a.style.left = pos.x + '%';
      a.style.top = pos.y + '%';
      a.dataset.stage = p.stageKey || 'ongoing';
      a.innerHTML = `<span class="map-marker__dot"></span><span class="map-marker__card">${p.image ? `<img src="${p.image}" alt="">` : ''}<b>${p.name}</b><small>${p.stage} · ${p.price}</small></span>`;
      inner.appendChild(a);
    });
    root.appendChild(inner);
  }

  /* ---------- suburb bar chart heights ---------- */
  $$('[data-bars]').forEach(el => {
    const values = JSON.parse(el.dataset.bars || '[]');
    const max = Math.max(...values.map(v => v.value || 0), 1);
    $$('i', el).forEach((bar, i) => {
      const v = values[i] || { value: 0 };
      bar.style.height = Math.max(8, ((v.value || 0) / max) * 100) + '%';
    });
  });

  /* ---------- FAQ deep-link ---------- */
  if (location.hash && $(location.hash)) {
    const item = $(location.hash).closest('.acc__item');
    if (item) item.classList.add('is-open');
  }
})();
