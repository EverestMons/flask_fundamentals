<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>survey</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='result.css') }}">
  </head>
  <body>
    <form action="/result" method="POST">
      <h4>Your Name:</h4><input name="name" type="text" /><br />
      <h4>Dojo Location:</h4>
      <select name="location">
        <option value="Chicago">Chicago</option>
        <option value="Silicon Valley">Silicon Valley</option>
        <option value="Seattle">Seattle</option>
        <option value="Los Angeles">Los Angeles</option>
        <option value="Dallas">Dallas</option>
        <option value="Washington DC">Washington DC</option>
        <option value="Berkeley">Berkeley</option>
        <option value="Orange County">Orange County</option>
      </select>
      <h4>Favorite Language: </h4>
      <select name="favlang">
        <option value="HTML">HTML</option>
        <option value="CSS">CSS</option>
        <option value="JavaScript">Javascript</option>
        <option value="Python">Python</option>
        <option value="Ruby">Ruby</option>
      </select>
    <h4>Comment (optional): </h4>
    <input name="comment" type="text"/><br />
    <input type="submit" value="Submit"/>
  </form>
  </body>
</html>
