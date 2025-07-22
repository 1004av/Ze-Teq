// index.js
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// 정적 파일 서비스 (예: public 폴더 안의 HTML, CSS, JS)
app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
