# flaskblog

This code is from Cory Schafer's tutorial series on youtube:</br>
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

It demonstrates how to build a Python Flask web app with registration & login via
oath, routing, database integration and more. 

To run app for yourself:
<ol>
  <li>Clone repository
  <li>Pip install requirements.txt
  <li>Update .env_sample with your info and rename to .env
    <ul>
      <li>The secret_key is used by WTForms to prevent CSRF attacks and also for 
      serializing our password reset tokens
      <li>the token_hex function from the secrets module is an easy way to generate
      your secret key
      <li>Use your own email address and pw for the email server (used for pw reset emails).
      <strong>NOTE:</strong> You may need to enable "less secure apps" access to your email temporarily if
      you receive a warning.
    </ul>
  <li>Run the app: <code>$ python run.py</code>
</ol>
