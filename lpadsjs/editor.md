
<div align="center">
<h1>LPEditor</h1>
<div id="map" style="width: 640px; height: 360px;"></div>
<br>
<form action="">
  <b>Place Name:</b>
  <input type="text" id="place">
  <br>
  <b>Location:</b>
  <input type="text" id="location">
  <br>
  <b>Host Name:</b>
  <input type="text" id="host">
  <br>
  <b>Link:</b>
  <input type="text" id="link">
  <br>
  <b>Pinlet Icon:</b>
  <input type="text" id="pinlet">
  <br>
  <b>WTA:</b>
  <input type="text" id="wta">
  <br>
  <b>Geocoded result:</b>
  <input type="text" id="town">
  <br>
  <b>Promo (JSON):</b>
  <input type="text" id="promo">
  <br>
  <button id="save" type="button">Save</button> 
  <button id="add" type="button">Add</button> 
  <button id="remove" type="button">Remove</button> 
  <button id="update" type="button">Update</button>
</form>
</div>

<link rel="stylesheet" href="https://unpkg.com/leaflet@latest/dist/leaflet.css" crossorigin=""/>
<style>
  .markdown-body img {
    background-color: transparent
  }
</style>
<script src="https://unpkg.com/leaflet@latest/dist/leaflet.js" crossorigin=""></script>
<script src="editormain.js"></script>
<script src="mapads.js"></script>