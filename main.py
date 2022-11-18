import streamlit as st
html_string = "<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="css/style.css" />
		<link rel="stylesheet" href="css/nivo-slider.css" type="text/css" media="screen" />
		<script src="jquery.nivo.slider.pack.js" type="text/javascript"></script>
        <title>Compra y Venta de Automotores</title>
    </head>
	<body id="home">
		<div id="wrapper">
			<header>
				<div id="logo">
				<h1>Ventas Oficiales<span id="iisrt"><span id="ii">II</span>  <span id="srt">MTGM</span></span></h1>
				<div id="tagline">
					<h2>Somos la Concecionaria N1 del Pais</h2>
				</div>
				</div>
			</header>
			<div class="slider-wrapper theme-default">
				<div id="slider" class="nivoSlider">
					<div id="home">
						<h1>Buscas comprar un vehiculo? Nosotros podemos ayudarte...</h1>
				</div>
			</div>
			<script type="text/javascript">
			$(window).load(function() {
				$('#slider').nivoSlider({pauseTime: 6000,});
			});
			</script>
			<footer>
				<p>Copyright (Mondino-Torres-Gomez-Mobili) </p>
			</footer>
		</div>			
	</body>
</html>"

st.markdown (html_string, unsafe_allow_html=true)
		
from data.dataFunctions import conectar , juntarDf, desconectar
from functions.functions import defineInterfaz
from functions.formulario import formInicial

con = conectar()
dataframe = juntarDf(con)


levelUser = formInicial()
defineInterfaz(levelUser,dataframe)

desconectar(con)


