function test() {
    alert("test succcess!");
}

var map;

function loadMapScenario() {
    map = new Microsoft.Maps.Map(document.getElementById('myMap'),
        {center:new Microsoft.Maps.Location(41.8, 123.38 ),});

}

function chooseData() {
    for (var i = 1; i <= 400; ++i) {
        if (typeof ($("#test" + i + "").attr("checked")) != "undefined") {
            console.log(document.getElementById("test" + i + "").parentElement.parentElement.id);
            console.log(document.getElementById("test" + i + "").id);
            $.ajax({
                type: "POST",
                url: '/chooseData',
                data: {
                    // Amenu: document.getElementById("test" + i + "").parentElement.parentElement.id,
                    Bmenu: i,
                },
                dataType: 'JSON',
            });
        }
    }

}

var Menus = [];

function runData() {
    var j = 0;
    var k = 0;

    for (var i = 1; i <= 400; ++i) {
        if (typeof ($("#test" + i + "").attr("checked")) != "undefined") {
            // console.log(document.getElementById("test" + i + "").parentElement.parentElement.id);
            // console.log(document.getElementById("test" + i + "").id);
            // Amenu[j++] = ;
            // Bmenu[k++] = document.getElementById("test" + i + "").id;
            // let tmpA={
            //     Amenu:document.getElementById("test" + i + "").parentElement.parentElement.id
            // };
            // let tmpB={
            //     Bmenu:document.getElementById("test" + i + "").id
            // };
            // Amenus.push(tmpA);
            // Bmenus.push(tmpB);
            var obj = {};
            obj.Amenu = document.getElementById("test" + i + "").parentElement.parentElement.id
            obj.Bmenu = document.getElementById("test" + i + "").id;
            Menus.push(obj);
            // console.(Menus);
            j++;
        }
    }

    $.ajax({
        type: "POST",
        url: '/rundata',
        data: JSON.stringify(Menus),

        dataType: 'JSON',
    });
}

function chooseAlg(e) {
    e.style.backgroundColor='rgb(250,250,250)'
    $.ajax({
        type: "POST",
        url: '/alg',
        data: {
            id: e.id,
        },
        dataType: 'JSON',
    });
}



function appendDAata() {

    for (var i = 1; i <= 100; ++i) {
        $('#normal_query').append(" <div class=\"form-check\">\n" +
            "                            <input class=\"form-check-input\" type=\"checkbox\" value=\"\" id=\"test" + i + "\" onclick=\"addChecked(this)\">\n" +
            "                            <label class=\"form-check-label\" for=\"test" + i + "\">\n" +
            "                               normal" + i + "\n" +
            "                            </label>\n" +
            "                        </div>"
        )
    }
    for (var i = 101; i <= 200; ++i) {
        var j = i - 100;
        $('#SHH-Taxi_query').append(" <div class=\"form-check\">\n" +
            "                            <input class=\"form-check-input\" type=\"checkbox\" value=\"\" id=\"test" + i + "\" onclick=\"addChecked(this)\">\n" +
            "                            <label class=\"form-check-label\" for=\"test" + i + "\">\n" +
            "                               SSH&nbsp&nbsp" + j + "\n" +
            "                            </label>\n" +
            "                        </div>"
        )
    }
    for (var i = 201; i <= 300; ++i) {
        var j = i - 200;
        $('#T-drive_query').append(" <div class=\"form-check\">\n" +
            "                            <input class=\"form-check-input\" type=\"checkbox\" value=\"\" id=\"test" + i + "\" onclick=\"addChecked(this)\">\n" +
            "                            <label class=\"form-check-label\" for=\"test" + i + "\">\n" +
            "                               T-Dri&nbsp" + j + "\n" +
            "                            </label>\n" + "                        </div>"
        )
    }
    for (var i = 301; i <= 400; ++i) {
        var j = i - 300;
        $('#uniform_query').append(" <div class=\"form-check\">\n" +
            "                            <input class=\"form-check-input\" type=\"checkbox\" value=\"\" id=\"test" + i + "\" onclick=\"addChecked(this)\">\n" +
            "                            <label class=\"form-check-label\" for=\"test" + i + "\">\n" +
            "                               uniform" + j + "\n" +
            "                            </label>\n" +
            "                        </div>"
        )
    }

}
var t=0;
function addChecked(e) {
    if (typeof ($(e).attr("checked")) == "undefined") {
        $(e).append("checked");
        $(e).attr('checked', true);
        $.ajax({
            type: "POST",
            url: 'showdata',
            data: {
                Amenu: e.parentElement.parentElement.id,
                Bmenu: e.id,
            },
            dataType: 'JSON',
        });
        if(t==0)
        {
            t=1;
            $.ajax({
                type: "GET",
                url: '/intidata',
                dataType: 'JSON',
                success: function (data) {
                    console.log(data.data)
                    var tmp=[];
                    if($(e).attr("checked")!= "undefined") {
                        for (var i = 0; i < 49; ++i) {
                            tmp.push(data.data[i]);
                        }
                    }
                    var center = new Microsoft.Maps.Location(tmp[0].longitude, tmp[0].latitude);
                    var pin = new Microsoft.Maps.Pushpin(center, {
                        color:'red'
                    });
                    map.entities.push(pin);
                    console.log(tmp);
                    for(var i=0;i<100;++i)
                    {


                        var coords = [new Microsoft.Maps.Location(tmp[i].longitude, tmp[i].latitude), new Microsoft.Maps.Location(tmp[i + 1].longitude, tmp[i + 1].latitude)]
                        console.log(coords);
                        var line = new Microsoft.Maps.Polyline(coords, {
                                strokeColor: 'red'
                            }
                        )
                        map.entities.push(line);
                    }

                }
            });
        }
    } else {
        // alert("faile/d");
        $(e).attr('checked', false);
    }
    $.ajax({
        type: "get",
        url: '/data',
        dataType: 'JSON',
        success: function (data) {
            console.log(data.data)
            var tmp=[];
            if($(e).attr("checked")!= "undefined") {
                for (var i = 0; i < 50; ++i) {
                    tmp.push(data.data[i]);
                }
            }
            var center = new Microsoft.Maps.Location(tmp[0].longitude, tmp[0].latitude);
            var pin = new Microsoft.Maps.Pushpin(center, {
                color:'grey'
            });
            map.entities.push(pin);
            console.log(tmp);
            for(var i=0;i<100;++i)
            {


                var coords = [new Microsoft.Maps.Location(tmp[i].longitude, tmp[i].latitude), new Microsoft.Maps.Location(tmp[i + 1].longitude, tmp[i + 1].latitude)]
                console.log(coords);
                var line = new Microsoft.Maps.Polyline(coords, {
                        strokeColor: 'grey',
                    },
                )
                map.entities.push(line);
            }

        }
    });
}