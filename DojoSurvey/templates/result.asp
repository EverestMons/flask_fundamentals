<%@ Language=VBScript %>
<html>
  <head>
    <meta charset="utf-8">
    <title>python form</title>
  </head>
  <body>
    <p>
      <%
      Response.Write("Name: " & request.form("name"))
      %>
    </p>

    <form action="/" >
        <input type="submit" value="Go Back" />
    </form>




  </body>
</html>
