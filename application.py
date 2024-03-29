import logging
import logging.handlers

from wsgiref.simple_server import make_server, WSGIServer
from SocketServer import ThreadingMixIn

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler 
LOG_FILE = '/tmp/sample-app/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

welcome = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <!--
    Copyright 2012 Amazon.com, Inc. or its affiliates. All Rights Reserved.

    Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

        http://aws.Amazon/apache2.0/

    or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
  -->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
  <link href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css" rel="stylesheet"/>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
 <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">


  <title>Welcome</title>
  <script>
    var lat ='';
  
  var lng ='';
  
   var map, infoWindow;
   
    $(document).ready(function(){
	$("#tableId").dataTable().fnClearTable();
		 $("#tableId").dataTable().fnDestroy();
	
	  $.ajax({
			url: "http://api.open-notify.org/astros.json", 
	   type: 'GET',
		dataType: 'json',
		cache: false,
		async: true,
		//contentType: "application/json",
		success: function(data) {
		console.log(data);
		$.each( data.people,function(key1,value){		
			$('#tableId').append('<tr><td>'+value.name+'</td><td>'+value.craft+'</td> </tr>')
		});	
		$('#tableId').DataTable({ width: '30%'}
		);
		}
	});
	
 $.ajax({
			url: "http://api.open-notify.org/iss-now.json", 
				dataType: 'json',
				success: function(data) {
					console.log("Success----->"+data);
					 lat = data.iss_position.latitude;
					 lng =   data.iss_position.longitude;
					
					 var iNumlat = parseFloat(lat);
					 var iNumlng = parseFloat(lng);
					 var latlng = new google.maps.LatLng(iNumlat,iNumlng);
					 map = new google.maps.Map(document.getElementById('somecomponent'), {
					center: latlng,
					zoom: 1
					});	
					
						var  marker = new google.maps.Marker({
								position: latlng,
								map: map,
								draggable: true
						});	     
					marker.setVisible(true);
	 console.log("done"+lat + '<-->'+ lng)
	
				
				},
				error: function (error) {
					console.log('error; ' + JSON.stringify(error));
				}
	});
	
 
	
  
	  
 
 
 $.getJSON('https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=37bda5b049e24780bfda4f38a4f50987', (response)=> {
      console.log('HELLO INSIDE response')
     // console.log('response', response)
	  
	 // console.log( response.articles  + ": " + response.articles.length );
	  
$.each( response.articles, function( key, value ) {
 console.log( JSON.stringify(key) + ": " + JSON.stringify(value)  );
 
  $('#TabsUL').append(' <li><a href="#tab'+key +'" >  <img src='+value.urlToImage+' width="100" height="70"  style="vertical-align:middle;margin-right:20px;">'+value.title+'</a> </li> ')
   $('#tabs').append('<div id="tab'+key+'"><h2>'+ value.description + '</h2> <p>'+ value.content+'</p> <p> Published At'+value.publishedAt+'</p></div>');
   
});
  
  
  
    }).done(function() {
	 $( "#tabs" ).tabs().addClass( "ui-tabs-vertical ui-helper-clearfix" );
    $( "#tabs li" ).removeClass( "ui-corner-top" ).addClass( "ui-corner-left" );
    console.log( "second success" );
  })
  .fail(function() {
    console.log( "error" );
  })
  .always(function() {
    console.log( "complete" );
  });
	
	
	
 });
	
	  
	  

	
 


      function initMap() {
        map = new google.maps.Map(document.getElementById('somecomponent'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 1
        });
        
}
	  





</script>
  <style>
     .ui-tabs-vertical { width: 55em; }
  .ui-tabs-vertical .ui-tabs-nav { padding: .2em .1em .2em .2em; float: left; width: 12em; }
  .ui-tabs-vertical .ui-tabs-nav li { clear: left; width: 100%; border-bottom-width: 1px !important; border-right-width: 0 !important; margin: 0 -1px .2em 0; }
  .ui-tabs-vertical .ui-tabs-nav li a { display:block; }
  .ui-tabs-vertical .ui-tabs-nav li.ui-tabs-active { padding-bottom: 0; padding-right: .1em; border-right-width: 1px; }
  .ui-tabs-vertical .ui-tabs-panel { padding: 1em; float: right; width: 40em;}
    #TabsUL {
  display:inline-table;
  }
  
  body {
    color: #1A0DAB;
    background-color: #E0E0E0;
    font-family: Arial, sans-serif;
    font-size:14px;
    -moz-transition-property: text-shadow;
    -moz-transition-duration: 4s;
    -webkit-transition-property: text-shadow;
    -webkit-transition-duration: 4s;
    text-shadow: none;
  }
  body.blurry {
    -moz-transition-property: text-shadow;
    -moz-transition-duration: 4s;
    -webkit-transition-property: text-shadow;
    -webkit-transition-duration: 4s;
    text-shadow: #fff 0px 0px 25px;
  }
  a {
    color: #0188cc;
  }
  .textColumn, .linksColumn {
    padding: 2em;
  }
  .textColumn {
    position: absolute;
    top: 0px;
    right: 50%;
    bottom: 0px;
    left: 0px;

    text-align: right;
    padding-top: 11em;
    background-color: #24B8EB;
  }
  .textColumn p {
    width: 75%;
    float:right;
  }
  .linksColumn {
    position: absolute;
    top:0px;
    right: 0px;
    bottom: 0px;
    left: 50%;
    background-color: #A9A9A9;
  }

  h1 {
    font-size: 500%;
    font-weight: normal;
    margin-bottom: 0em;
  }
  h2 {
    font-size: 200%;
    font-weight: normal;
    margin-bottom: 0em;
  }
  ul {
    padding-left: 1em;
    margin: 0px;
  }
  li {
    margin: 1em 0em;
  }
    #tableId_wrapper{
  width :500px;
  }
  </style>
</head>
<body id="sample">
 
    
  <div id="div1"   style="border:2px solid magenta;width:fit-content;"> 
   <p style="font-size:22px;"> How Many People Are In Space Right Now  </p>
  <table id="tableId" class="table table-condensed responsive" >
     <thead>
            <tr>
                <th>Name</th>
                <th>Craft</th>
            </tr>
        </thead>
    </tbody>
</table>
</div>
  <div id="div2"   style="border:2px solid magenta;width:fit-content;"> 
   <p style="font-size:22px;"> Current Location  </p>
  <div id="somecomponent" style="width: 500px; height: 400px;"></div>
</div>

 <div id="tabs">
  <ul id="TabsUL">
   
  </ul>
 

  </div>


</body>
</html>

 <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAPu_mcAMtQA_Rnr4bKKPo9kV6ZEPY-kBI&callback=initMap">
    </script>
"""

def application(environ, start_response):
    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']
    if method == 'POST':
        try:
            if path == '/':
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size)
                logger.info("Received message: %s" % request_body)
            elif path == '/scheduled':
                logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'], environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
        response = ''
    else:
        response = welcome
    status = '200 OK'
    headers = [('Content-type', 'text/html')]

    start_response(status, headers)
    return [response]

class ThreadingWSGIServer(ThreadingMixIn, WSGIServer): 
    pass

if __name__ == '__main__':
    httpd = make_server('', 8000, application, ThreadingWSGIServer)
    print "Serving on port 8000..."
    httpd.serve_forever()
