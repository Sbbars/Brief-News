window.onscroll = function() {scrollFunction()};
        
        function scrollFunction() {
          if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
            document.getElementById("navbar").style.padding = "25px 25px";
            document.getElementById("logo").style.fontSize = "25px";
          } else {
            document.getElementById("navbar").style.padding = " 25px 25px";
            document.getElementById("logo").style.fontSize = "30px";
          }
        }

       
