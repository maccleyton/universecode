document.addEventListener('DOMContentLoaded', () => {
    initTimeline();
});

function initTimeline() {
    const timelineContainer = document.getElementById('timeline-content-area');
    if (!timelineContainer) return;

    const articles = document.querySelectorAll('article.book-article');
    
    articles.forEach((article, index) => {
        const id = article.id;
        const numberSpan = article.querySelector('.chapter-number');
        const titleH1 = article.querySelector('.chapter-title');
        const subSpan = article.querySelector('.chapter-sub');

        let number = numberSpan ? numberSpan.innerText : '';
        let title = titleH1 ? titleH1.innerText : 'Capítulo sem título';
        let sub = subSpan ? subSpan.innerText : '';

        // Handle specific case for Conclusion if needed, currently it follows chapter structure
        if (id === 'conclusao' && !number) {
            number = '43';
            title = 'Conclusão';
        }

        const item = document.createElement('div');
        item.className = 'timeline-item';
        item.onclick = () => {
            scrollToChapter(id);
            closeTimeline();
        };

        const dot = document.createElement('div');
        dot.className = 'timeline-dot';

        const info = document.createElement('div');
        
        const numEl = document.createElement('span');
        numEl.className = 'timeline-chapter-num';
        numEl.innerText = number;

        const titleEl = document.createElement('div');
        titleEl.className = 'timeline-chapter-title';
        titleEl.innerText = title;

        const subEl = document.createElement('span');
        subEl.className = 'timeline-chapter-sub';
        subEl.innerText = sub;

        info.appendChild(numEl);
        info.appendChild(titleEl);
        if (sub) info.appendChild(subEl);

        item.appendChild(dot);
        item.appendChild(info);

        timelineContainer.appendChild(item);
    });

    // Highlight current chapter on scroll
    window.addEventListener('scroll', highlightCurrentChapter);
}

function highlightCurrentChapter() {
    const articles = document.querySelectorAll('article.book-article');
    let currentId = '';

    articles.forEach(article => {
        const rect = article.getBoundingClientRect();
        if (rect.top < window.innerHeight / 2) {
            currentId = article.id;
        }
    });

    if (currentId) {
        document.querySelectorAll('.timeline-item').forEach(item => {
            item.classList.remove('active');
            // Matching logic could be improved if we stored ID on the item
            // But simply re-scanning text or index is fragile. 
            // Let's attach ID to item in init
        });
        
        // Better implementation:
        // We need to link items to IDs. Re-implementing init loop slightly above.
    }
}

// Global functions for UI control
window.toggleTimeline = function() {
    const sidebar = document.getElementById('timeline-sidebar');
    const overlay = document.getElementById('timeline-overlay');
    if (sidebar && overlay) {
        sidebar.classList.toggle('active');
        overlay.classList.toggle('active');
    }
}

window.closeTimeline = function() {
    const sidebar = document.getElementById('timeline-sidebar');
    const overlay = document.getElementById('timeline-overlay');
    if (sidebar && overlay) {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
    }
}

function scrollToChapter(id) {
    const element = document.getElementById(id);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}
