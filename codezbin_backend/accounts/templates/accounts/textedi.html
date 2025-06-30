<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Codezbin Editor</title>
  <link rel="stylesheet" href="{% static 'accounts/css/textedi.css' %}">
  <style>
    .editor-container {
      display: flex;
      height: 90vh;
    }
    .editor-main {
      flex: 1;
      padding: 20px;
      background-color: #0b1f3a;
      color: #e4e9f1;
    }
    .code-box {
      width: 100%;
      height: 300px;
      background-color: #17335f;
      color: white;
      font-family: monospace;
      padding: 10px;
      font-size: 16px;
    }
    .output-box {
      margin-top: 20px;
      background-color: #112649;
      padding: 10px;
      color: #00f2fe;
    }
    .editor-sidebar {
      width: 250px;
      background-color: #08152e;
      color: white;
      padding: 20px;
      overflow-y: auto;
    }
    .language-list label {
      display: block;
      margin-top: 10px;
      cursor: pointer;
    }
    .selected-lang {
      margin-top: 15px;
      font-weight: bold;
      color: #00c896;
    }
    .run-btn {
      margin-top: 20px;
      background-color: #00f2fe;
      color: black;
      border: none;
      padding: 10px 20px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <header class="top-nav">
    <div class="nav-left"><h2 style="color:#00f2fe;">CODEZBIN</h2></div>
  </header>

  <form method="POST" action="{% url 'run_code' %}">
    {% csrf_token %}
    <div class="editor-container">
      <div class="editor-main">
        <textarea name="code" class="code-box">{% if code %}{{ code }}{% else %}// Write your code here{% endif %}</textarea>


        <div class="output-box">
          {% if output %}
            <strong>Output:</strong>
            <pre>{{ output }}</pre>
          {% else %}
            <pre>// Output will appear here</pre>
          {% endif %}
        </div>

        <div class="selected-lang">Language: <span id="selectedLang">{{ language|default:"C" }}</span></div>
        <input type="hidden" name="language" id="languageInput" value="{{ language|default:'c' }}" />

        <button type="submit" class="run-btn">Run</button>
      </div>

      <aside class="editor-sidebar">
        <h3>Select Language</h3>
        <div class="language-list">
          <label><input type="radio" name="lang" value="c" checked> C</label>
          <label><input type="radio" name="lang" value="cpp"> C++</label>
          <label><input type="radio" name="lang" value="python"> Python</label>
          <label><input type="radio" name="lang" value="java"> Java</label>
          <label><input type="radio" name="lang" value="js"> JavaScript</label>
          <label><input type="radio" name="lang" value="go"> Go</label>
          <label><input type="radio" name="lang" value="sql"> SQL</label>
          <label><input type="radio" name="lang" value="csharp"> C#</label>
          <label><input type="radio" name="lang" value="swift"> Swift</label>
          <label><input type="radio" name="lang" value="kotlin"> Kotlin</label>
          <label><input type="radio" name="lang" value="php"> PHP</label>
        </div>
      </aside>
    </div>
  </form>

  <script>
    const radios = document.querySelectorAll('input[name="lang"]');
    const selectedLang = document.getElementById('selectedLang');
    const languageInput = document.getElementById('languageInput');

    radios.forEach(radio => {
      radio.addEventListener('change', function () {
        selectedLang.textContent = this.value.toUpperCase();
        languageInput.value = this.value;
      });
    });
  </script>
</body>
</html>
