window.onscroll = function() {scrollFunction()};
        
        function scrollFunction() {
          if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
            document.getElementById("navbar").style.padding = "5px 5px";
            document.getElementById("logo").style.fontSize = "25px";
          } else {
            document.getElementById("navbar").style.padding = " 15px 15px";
            document.getElementById("logo").style.fontSize = "25px";
          }
        }

       
