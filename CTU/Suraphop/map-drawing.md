### 🧑‍💻 Mr.Suraphop
- Step 1111: ...
- Step 2222: ...
- Step 3333: ....
- **Code Snippet:**
  ``` 
  router.post('/', async (req, res) => {
  const start = Date.now();
  
  await doLoginCheck();

  const duration = Date.now() - start;
  console.log(`[api_login] took ${duration}ms`);
  res.json({ success: true });
});


