document.addEventListener('DOMContentLoaded', () => {
  const likeBtn = document.getElementById('like-btn');
  if (likeBtn) {
    likeBtn.addEventListener('click', async () => {
      const url = likeBtn.getAttribute('data-like-url');
      try {
        const res = await fetch(url, { method: 'POST' });
        const data = await res.json();
        if (data.ok) {
          const count = document.getElementById('like-count');
          if (count) count.textContent = data.likes;
        }
      } catch (err) {
        console.error('Error al hacer like:', err);
      }
    });
  }
});