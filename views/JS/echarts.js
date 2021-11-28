var n;
function sumN() {
    n=1;
    $.ajax({
        type: "GET",
        url: '/sumN',
        async: false,
        dataType: 'JSON',
        success: function (data) {
            n=data.data;
        }
    });
}
function setRuntime(){
    var chartDom = document.getElementById('runtime');
    var myChart = echarts.init(chartDom);
    var obj=
        {

            type: 'line',
            smooth: true,

            data: []
        };
    var option;
    option = {
        title:{
            text:'Performance Evaluation on Distance threshold τ'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            y:338,
            x:40,
            itemHeight: 7,
            data: []
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data:["256","512","1024"]
        },
        yAxis: {
            type: 'value',
            name:'t/s'
        },
        series: [

            {
                // name:,
                type: 'line',
                smooth: true,
                data: []}

        ],




    };
    if(n==3) {

        option.series.push(obj);
        option.series.push(obj);

        console.log(option.series);
        $.get('dataTime.json').done(function(data)
        {
            myChart.setOption({
                 legend: {
                        y:338,
                        x:40,
                        itemHeight: 7,
                        data: data.legend
                 },
                    series: [
                        {
                            // name:"LCSS",
                            name:data.data.legend[0],
                            data: data.data.Lcssdata
                        },
                        {
                             // name:"DTW",
                            name:data.data.legend[1],
                            data: data.data.DTWdata
                        },
                        {
                            // name:"Secure",
                            name:data.data.legend[2],
                            data:data.data.Securedata
                        }
                    ]
                }
            );
        });
    }
    else if(n==2){
        option.series.push(obj);
        console.log(option.series);
        $.get('dataTime.json').done(function(data)
        {
            if(data.data.legend[0]=="SLCSS"&&(data.data.legend[1]=="SDTW")) {
                myChart.setOption({
                        legend: {
                            y: 338,
                            x:40,
                            itemHeight: 7,
                            data: data.legend
                        },

                        series: [
                            {
                                // name:data.name,
                                name: data.data.legend[0],
                                data: data.data.Lcssdata
                            },
                            {
                                // name:data.name,
                                name: data.data.legend[1],
                                data: data.data.DTWdata
                            },
                        ]
                    }
                );
            }else if(data.data.legend[1]=="SLCSS"&&(data.data.legend[0]=="SDTW")){
                myChart.setOption({
                        legend: {
                            y: 338,
                            x:40,
                            itemHeight: 7,
                            data: data.legend
                        },

                        series: [
                            {
                                // name:data.name,
                                name: data.data.legend[0],
                                data: data.data.DTWdata
                            },
                            {
                                // name:data.name,
                                name: data.data.legend[1],
                                data: data.data.Lcssdata
                            },
                        ]
                    }
                );
            }else if(data.data.legend[0]=="SLCSS"&&(data.data.legend[1]=="SBD")) {
                myChart.setOption({
                        legend: {
                            y: 338,
                            x:40,
                            itemHeight: 7,
                            data: data.legend
                        },

                        series: [
                            {
                                // name:data.name,
                                name: data.data.legend[0],
                                data: data.data.Lcssdata
                            },
                            {
                                // name:data.name,
                                name: data.data.legend[1],
                                data: data.data.Securedata
                            },
                        ]
                    }
                );
            }else if(data.data.legend[1]=="SLCSS"&&(data.data.legend[0]=="SBD")){
                myChart.setOption({
                        legend: {
                            y: 338,
                            x:40,
                            itemHeight: 7,
                            data: data.legend
                        },

                        series: [
                            {
                                // name:data.name,
                                name: data.data.legend[0],
                                data: data.data.Securedata
                            },
                            {
                                // name:data.name,
                                name: data.data.legend[1],
                                data: data.data.Lcssdata
                            },
                        ]
                    }
                );
            }else if(data.data.legend[0]=="SDTW"&&(data.data.legend[1]=="SBD")){
                myChart.setOption({
                        legend: {
                            y:338,
                            x:40,
                            itemHeight: 7,
                            data: data.legend
                        },
                        series: [
                            {
                                // name:data.name,
                                name:data.data.legend[0],
                                data: data.data.DTWdata
                            },
                            {
                                // name:data.name,
                                name:data.data.legend[1],
                                data: data.data.Securedata
                            },
                        ]
                    }
                );
            }else if(data.data.legend[1]=="SDTW"&&(data.data.legend[0]=="SBD")){
                myChart.setOption({
                        legend: {
                            y:338,
                            x:40,
                            itemHeight: 7,
                            data: data.legend
                        },
                        series: [
                            {
                                // name:data.name,
                                name:data.data.legend[0],
                                data: data.data.Securedata
                            },
                            {
                                // name:data.name,
                                name:data.data.legend[1],
                                data: data.data.DTWdata
                            },
                        ]
                    }
                );
            }

        });
    }
    else{
        $.get('dataTime.json').done(function(data)
        {
            if(data.data.legend[0]=="SLCSS") {
                myChart.setOption({
                        legend: {
                            y:338,
                            x:40,
                            itemHeight: 7,
                            data: data.legend
                        },
                        series: [
                            {
                                // name:data.name,
                                name:data.data.legend[0],
                                data: data.data.Lcssdata
                            },
                        ]
                    }
                );
            }else if(data.data.legend[0]=="SDTW"){
                myChart.setOption({
                        legend: {
                            y:338,
                            x:40,
                            itemHeight: 7,
                            data: data.legend
                        },
                        series: [
                            {
                                // name:data.name,
                                name:data.data.legend[0],
                                data: data.data.DTWdata
                            },
                        ]
                    });
            }else {
                    myChart.setOption({
                            legend: {
                                y:338,
                                x:40,
                                itemHeight: 7,
                                data: data.legend
                            },
                            series: [
                                {
                                    // name:data.name,
                                    name: data.data.legend[0],
                                    data: data.data.Securedata
                                },
                            ]
                        }
                    );
                }
        });
    }
    console.log(option.legend)
    option && myChart.setOption(option);
}
function setMemory(){
    console.log(n)
    var chartDom = document.getElementById('memory');
    var myChart = echarts.init(chartDom);
    var obj=
        {
            // name:,
            type: 'line',
            smooth: true,
            // seriesLayoutBy: 'row',
            // emphasis: {focus: 'series'},
            data: []
        };
    var option;
    option = {
        title:{
            // left:"5%",
            text:'Performance Evaluation on Top-k'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            y:338,
            x:40,
            itemHeight: 7,
            data: []
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data:["10","50","100","200"],
        },
        yAxis: {
            type: 'value',
            name:'t/s'
        },
        series: [
            {
                // name:,
                type: 'line',
                smooth: true,
                data: []}
        ]
    };
    if(n==3) {
        option.series.push(obj);
        option.series.push(obj);
        // console.log(obj);
        console.log(option.series);
        $.get('dataAverage.json').done(function(data)
        {
            myChart.setOption({
                    legend: {
                        y:338,
                        x:40,
                        itemHeight: 7,
                        data: data.legend
                    },
                    series: [
                        {
                            // name:data.name,
                            name: data.data.legend[0],
                            data: data.data.Lcssdata
                        },
                        {
                            // name:data.name,
                            name: data.data.legend[1],
                            data: data.data.DTWdata
                        },
                        {
                            // name:data.name,
                            name: data.data.legend[2],
                            data:data.data.Securedata
                        }
                    ]
                }
            );
        });
    }
    else if(n==2){
        option.series.push(obj);
        console.log(option.series);
        $.get('dataAverage.json').done(function(data)
        {
            myChart.setOption({
                    legend: {
                        y:338,
                        x:40,
                        itemHeight: 7,
                        data: data.legend
                    },
                    series: [
                        {
                            // name:data.name,
                            name: data.data.legend[0],
                            data: data.data.Lcssdata
                        },
                        {
                            // name:data.name,
                            name: data.data.legend[1],
                            data: data.data.DTWdata
                        },
                    ]
                }
            );
        });
    }
    else{
        $.get('dataAverage.json').done(function(data)
        {
            myChart.setOption({
                    legend: {
                        y:338,
                        x:40,
                        itemHeight: 7,
                        data: data.legend
                    },
                    series: [
                        {
                            // name:data.name,
                            name: data.data.legend[0],
                            data: data.data.DTWdata
                        },
                    ]
                }
            );
        });
    }
    option && myChart.setOption(option);
}

function test2(){
    var chartDom = document.getElementById('c2');
    var myChart = echarts.init(chartDom);
    var obj=
        {

            type: 'line',
            smooth: true,

            data: []
        };
    var option;
    option = {
        title:{
            // left:"5%",
            text:'Performance Evaluation on Key size K'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            y:338,
            x:40,
            itemHeight: 7,
            data: []
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            data:["1","2","3","4"]
        },
        yAxis: {
            type: 'value',
            name:'t/s',
        },
        series: [
            {
                // name:,
                type: 'line',
                smooth: true,
                data: []}
        ]
    };
    if(n==3) {
        option.series.push(obj);
        option.series.push(obj);
        // console.log(obj);
        console.log(option.series);
        $.get('dataMemory.json').done(function(data)
        {
            myChart.setOption({
                    legend: {
                        y:338,
                        x:40,
                        itemHeight: 7,
                        data: data.legend
                    },
                    series: [
                        {
                            // name:data.name,
                            name: data.data.legend[0],
                            data: data.data.Lcssdata
                        },
                        {
                            // name:data.name,
                            name: data.data.legend[1],
                            data: data.data.DTWdata
                        },
                        {
                            // name:data.name,
                            name: data.data.legend[2],
                            data:data.data.Securedata
                        }
                    ]
                }
            );
        });
    }
    else if(n==2){
        option.series.push(obj);
        console.log(option.series);
        $.get('dataMemory.json').done(function(data)
        {
            myChart.setOption({
                    legend: {
                        y:338338,
                        x:40,
                        itemHeight: 7,
                        data: data.legend
                    },
                    series: [
                        {
                            // name:data.name,
                            name: data.data.legend[0],
                            data: data.data.Lcssdata
                        },
                        {
                            // name:data.name,
                            name: data.data.legend[1],
                            data: data.data.DTWdata
                        },
                    ]
                }
            );
        });
    }
    else{
        $.get('dataMemory.json').done(function(data)
        {
            myChart.setOption({
                    legend: {
                        y:338,
                        x:40,
                        itemHeight: 7,
                        data: data.legend
                    },
                    series: [
                        {
                            // name:data.name,
                            name: data.data.legend[0],
                            data: data.data.DTWdata
                        },
                    ]
                }
            );
        });
    }
    option && myChart.setOption(option);
}

function appendTable(){

    console.log(n)
    $.ajax({
        type: "get",
        url: '/alg1',
        async: false,
        dataType: 'JSON',
        success: function (data) {
           var tmp;
            tmp=data.data.Algorithm;
            document.getElementById('alg1').innerHTML=tmp;
            tmp=data.data.Simliarty;
            document.getElementById('alg1k').innerHTML=tmp;
        }
    });
    if(n>=2)
    {

        $('#tableHead').append("  <th scope=\"col\" id=\"alg2\"></th>")
        $('#tableBody').append("  <td scope=\"col\" id=\"alg2k\"></td>")

        $.ajax({
            type: "get",
            url: '/alg2',
            async: false,
            dataType: 'JSON',
            success: function (data) {
                var tmp
                tmp=data.data.Algorithm;
                document.getElementById('alg2').innerHTML=tmp;
                tmp=data.data.Simliarty;
                document.getElementById('alg2k').innerHTML=tmp;
            }
        });
    }
    if(n==3)
    {
        $('#tableHead').append("  <th scope=\"col\" id=\"alg3\"></th>")
        $('#tableBody').append("  <td scope=\"col\" id=\"alg3k\"></td>")

        $.ajax({
            type: "get",
            url: '/alg3',
            async: false,
            dataType: 'JSON',
            success: function (data) {
                var tmp
                tmp=data.data.Algorithm;
                document.getElementById('alg3').innerHTML=tmp;
                tmp=data.data.Simliarty;
                document.getElementById('alg3k').innerHTML=tmp;
            }
        });
    }
}