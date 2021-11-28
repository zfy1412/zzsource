package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"mapweb/send"
	"net/http"
	"strconv"
)

var key int64
var chooseData [1000]int
var chosen  [30]string
var ci int
var i int


func main() {
	i = 0
	ci =0
	r := gin.Default()
	r.LoadHTMLGlob("HTML/*")
	r.StaticFS("/views", http.Dir("./views/"))
	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "new map.html", nil)
	})
	r.GET("/line.html", func(c *gin.Context) {
		c.HTML(http.StatusOK, "line.html", nil)
	})

	r.POST("/showdata", func(c *gin.Context) {
		//value1:=c.PostForm("Amenu")
		value2 := c.PostForm("Bmenu")
		//fmt.Println("val:",value1,value2)
		key = send.Select(value2)
		fmt.Println(key)
	})
	r.GET("/intidata", func(c *gin.Context) {
		datab:=send.Yread(key)
		//fmt.Println(datab)
		c.JSON(http.StatusOK,gin.H{
			"data":datab,
		})

	})

	r.GET("/data", func(c *gin.Context) {
		//c.HTML(http.StatusOK, "newmap.html", nil)
		datas := send.Read(key)
		//datas:=send.Try()
		c.JSON(http.StatusOK, gin.H{
			"data": datas,
		})
	})

	r.POST("/chooseData", func(c *gin.Context) {
		//value1:=c.PostForm("Amenu")
		value := c.PostForm("Bmenu")
		//chooseData[i],_= strconv.ParseInt(value, 10, 32)
		chooseData[i], _ = strconv.Atoi(value)
		fmt.Println("val:", chooseData[i])
		i++
	})



	r.POST("/alg", func(c *gin.Context) {
		chosen[ci]=c.PostForm("id")
		ci++
		fmt.Println("val:", chosen)
	})

	r.GET("/sumN", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"data": ci,
		})
	})



	r.GET("/dataTime.json", func(dataTime *gin.Context) {
		var keylengthtimelcss [100]float64
		var keylengthtimedtw [100]float64
		var keylengthtime3 [100]float64
		var ke1 float64
		ke1 = 0
		var ke2 float64
		ke2 = 0
		var ke3 float64
		ke3=0
		var Keylength = [3]int{256, 512, 1024}
		for k := 0; k < 3; k++ {
			for j := 0; j < i; j++ {
				_, ke2 = send.DTWPrint(Keylength[k], chooseData[j])
				keylengthtimedtw[k] = keylengthtimedtw[k] + ke2
				_, ke1 = send.LcssPrint(Keylength[k], chooseData[j], 10)
				keylengthtimelcss[k] = keylengthtimelcss[k] + ke1
				_,ke3 = send.SecurePrint(Keylength[k],chooseData[j],10)
				keylengthtime3[k]=keylengthtime3[k]+ke3
			}
		}

		te := send.Runtime(chosen,ci,keylengthtimelcss,keylengthtimedtw,keylengthtime3)
		fmt.Println(te)
		dataTime.JSON(http.StatusOK, gin.H{"data": te})
	})
	r.GET("/dataAverage.json", func(c *gin.Context) {
		var keytoplcss [100]float64
		var keytopdtw [100]float64
		var keytopse [100]float64
		var keythreshold3 =[4]int{10,50,100,200}
		var ke1 float64
		ke1 = 0
		var ke2 float64
		ke2 = 0
		var ke3 float64
		ke3=0
		for k := 0; k < 4; k++ {
			for j := 0; j < i; j++ {
				_, ke2 = send.DTWPrint(keythreshold3[k], chooseData[j])
				keytopdtw[k] = keytopdtw[k] + ke2
				_, ke1 = send.LcssPrint(keythreshold3[k], chooseData[j], 10)
				keytoplcss[k] = keytoplcss[k] + ke1
				_,ke3 = send.SecurePrint(keythreshold3[k],chooseData[j],10)
				keytopse[k]=keytopse[k]+ke3
			}
		}


		average := send.Average(chosen,ci,keytoplcss,keytopdtw,keytopse)
		//fmt.Println(average)
		c.JSON(http.StatusOK, gin.H{"data": average})
	})
	r.GET("/dataMemory.json", func(c *gin.Context) {
		var keythresholdlcss [100]float64
		var keythresholddtw [100]float64
		var keythresholdse [100]float64
		var dtwkeythreshold float64
		var ke1 float64
		ke1 = 0
		var ke2 float64
		ke2 = 0
		var ke3 float64
		ke3=0
		for k := 0; k < 5; k++ {
			for j := 0; j < i; j++ {
				_, ke1 = send.LcssPrint(256, chooseData[j],10)
				keythresholdlcss[k] = keythresholdlcss[k] + ke1
				_, ke2 = send.DTWPrint(256, chooseData[j])
				dtwkeythreshold = dtwkeythreshold + ke2
				_,ke3 = send.SecurePrint(256,chooseData[j],10)
				keythresholdse[k]=keythresholdse[k]+ke3
			}
			keythresholddtw[k] = dtwkeythreshold
		}
		me := send.Mermory(chosen,ci,keythresholdlcss,keythresholddtw,keythresholdse)
		//fmt.Println(me)
		c.JSON(http.StatusOK, gin.H{"data": me})
	})


	//echarts

	r.GET("/alg1", func(c *gin.Context) {
		a:=send.Select1()
		c.JSON(http.StatusOK, gin.H{
			"data": a,
		})
	})
	r.GET("/alg2", func(c *gin.Context) {
		a:=send.Select2()
		c.JSON(http.StatusOK, gin.H{
			"data": a,
		})
	})
	r.GET("/alg3" , func(c *gin.Context) {
		a:=send.Select3()
		c.JSON(http.StatusOK, gin.H{
			"data": a,
		})
	})





	r.Run(":8090")
}

