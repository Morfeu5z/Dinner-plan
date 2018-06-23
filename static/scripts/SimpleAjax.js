
    /**
     * Funkcja sprawdza czy możliwe jest wykożystanie ajax'a
     * @returns {*} objekt dla żądania ajax
     */
    function tryAjaxVersion() {
        var xmlHttp;
        try {
            xmlHttp = new XMLHttpRequest();
        } catch (e) {
            try {
                xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
            } catch (e) {
                try {
                    xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
                } catch (e) {
                    alert("Your browser does not support AJAX!");
                    return false;
                }
            }
        }
        return xmlHttp;
    }

    /**
     * Funkcja wykożystuje ajax
     * Przesyłamy listę parametrów jako array [[1, 'a'],[2, 'b']]
     * Funkcja zwraca parametry z serwera jako json i konwertuje do array list [[1, 'a'],[2, 'b']]
     * Można ustalic metodę
     * Można ustalić ścieżkę
     * @param dict : array with elements - parametry do przesłania [[1, 'a'],[2, 'b']]
     * @param path : string - ścieżka docelowa
     * @param method : string - metoda wysłania
     * @returns {*[]|*} : array with string elements - zwraca tablicę z danymi [[1, 'a'],[2, 'b']]
     * @Key_Name_In_Json 'param' - a w środku parametry w formie tablicy
     */
    function simpleAjax(list = [1, 'string'], path = 'SAT', method = 'POST') {
        dict = {'param': list};
        var Request = tryAjaxVersion();
        if (Request != false) {
            Request.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    localStorage.jsonfromajaxresponse = this.response;
                }
            };
            Request.open(method, path);
            var data_to_send = JSON.stringify(dict)
            console.log("Json to send: " + data_to_send);
            Request.send(data_to_send);
        }
        var param = localStorage.jsonfromajaxresponse;
        param = JSON.parse(param);
        localStorage.removeItem('jsonfromajaxresponse');
        return param.param;
    }
