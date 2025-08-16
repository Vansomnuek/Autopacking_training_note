### 🧑‍💻 Sikarin
- CTU coding
- **Code Snippet:**
```javascript
router.post('/', async (req, res) => {
  const start = Date.now();
  
  await doLoginCheck();

  const duration = Date.now() - start;
  console.log(`[api_login] took ${duration}ms`);

  res.json({ success: true });
});
```
