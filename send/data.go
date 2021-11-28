package send

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)
type Datanew struct{
	X float64 `json:"latitude"`
	Y float64 `json:"longitude"`
}
var datas[10000] Datanew
var bidui[10000] Datanew
func Yread(key int64) [10000]Datanew{
	if key>=1 && key<=100 {
		c := fmt.Sprintf("%s", "./resource/query/normal_query.csv")
		f, err := os.Open(c)
		if err != nil {
			fmt.Println(err)
		}
		var a, b float64
		defer f.Close()
		buff := bufio.NewReader(f)
		for i:=0;i<100;i++{
			line, err := buff.ReadString('\n')
			if err == io.EOF {
				break
			}
			tmp := strings.Split(line, ",")
			a, _ = strconv.ParseFloat(tmp[0], 64)
			//string([]byte(tmp[1])[:len(tmp[1]) - 2])
			b, _ = strconv.ParseFloat(strings.Split(tmp[1], "\n")[0], 64)
			bidui[i].X=a
			bidui[i].Y=b
		}
	}else if key>=101&&key<=200{
		c := fmt.Sprintf("%s", "./resource/query/SHH-Taxi_query.csv")
		f, err := os.Open(c)
		if err != nil {
			fmt.Println(err)
		}
		var a, b float64
		defer f.Close()
		buff := bufio.NewReader(f)
		for i:=0;i<100;i++{
			line, err := buff.ReadString('\n')
			if err == io.EOF {
				break
			}
			tmp := strings.Split(line, ",")
			a, _ = strconv.ParseFloat(tmp[0], 64)
			//string([]byte(tmp[1])[:len(tmp[1]) - 2])
			b, _ = strconv.ParseFloat(strings.Split(tmp[1], "\n")[0], 64)
			bidui[i].X=a
			bidui[i].Y=b
		}
	}else if key>=201&&key<=300 {
		c := fmt.Sprintf("%s", "./resource/query/T-drive_query.csv")
		f, err := os.Open(c)
		if err != nil {
			fmt.Println(err)
		}
		var a, b float64
		defer f.Close()
		buff := bufio.NewReader(f)
		for i:=0;i<100;i++{
			line, err := buff.ReadString('\n')
			if err == io.EOF {
				break
			}
			tmp := strings.Split(line, ",")
			a, _ = strconv.ParseFloat(tmp[0], 64)
			//string([]byte(tmp[1])[:len(tmp[1]) - 2])
			b, _ = strconv.ParseFloat(strings.Split(tmp[1], "\n")[0], 64)
			bidui[i].X=a
			bidui[i].Y=b
		}
	}else if key>=301&&key<=400 {
		c := fmt.Sprintf("%s", "./resource/query/uniform_query.csv")
		f, err := os.Open(c)
		if err != nil {
			fmt.Println(err)
		}
		var a, b float64
		defer f.Close()
		buff := bufio.NewReader(f)
		for i:=0;i<100;i++{
			line, err := buff.ReadString('\n')
			if err == io.EOF {
				break
			}
			tmp := strings.Split(line, ",")
			a, _ = strconv.ParseFloat(tmp[0], 64)
			//string([]byte(tmp[1])[:len(tmp[1]) - 2])
			b, _ = strconv.ParseFloat(strings.Split(tmp[1], "\n")[0], 64)
			bidui[i].X=a
			bidui[i].Y=b
		}

	}
	//fmt.Println(bidui)
	return bidui
}
func Read(key int64) [10000]Datanew{
	if key>=1 && key<=100 {
		c := fmt.Sprintf("%s%05d%s", "./resource/normal/normal_", key, ".csv")
		f, err := os.Open(c)
		if err != nil {
			fmt.Println(err)
		}
		var a, b float64
		defer f.Close()
		buff := bufio.NewReader(f)
		for i:=0;i<100;i++{
			line, err := buff.ReadString('\n')
			if err == io.EOF {
				break
			}
			tmp := strings.Split(line, ",")
			a, _ = strconv.ParseFloat(tmp[0], 64)
			//string([]byte(tmp[1])[:len(tmp[1]) - 2])
			b, _ = strconv.ParseFloat(strings.Split(tmp[1], "\n")[0], 64)
			datas[i].X=a
			datas[i].Y=b
		}
	}else if key>=101&&key<=200{
		c := fmt.Sprintf("%s%05d%s", "./resource/SHH-Taxi/SHH-Taxi_", key-100, ".csv")
		f, err := os.Open(c)
		if err != nil {
			fmt.Println(err)
		}
		var a, b float64
		defer f.Close()
		buff := bufio.NewReader(f)
		for i:=0;i<100;i++{
			line, err := buff.ReadString('\n')
			if err == io.EOF {
				break
			}
			tmp := strings.Split(line, ",")
			a, _ = strconv.ParseFloat(tmp[0], 64)
			//string([]byte(tmp[1])[:len(tmp[1]) - 2])
			b, _ = strconv.ParseFloat(strings.Split(tmp[1], "\n")[0], 64)
			datas[i].X=a
			datas[i].Y=b
		}
	}else if key>=201&&key<=300 {
		c := fmt.Sprintf("%s%05d%s", "./resource/T-drive/T-drive_", key-200, ".csv")
		f, err := os.Open(c)
		if err != nil {
			fmt.Println(err)
		}
		var a, b float64
		defer f.Close()
		buff := bufio.NewReader(f)
		for i:=0;i<100;i++{
			line, err := buff.ReadString('\n')
			if err == io.EOF {
				break
			}
			tmp := strings.Split(line, ",")
			a, _ = strconv.ParseFloat(tmp[0], 64)
			//string([]byte(tmp[1])[:len(tmp[1]) - 2])
			b, _ = strconv.ParseFloat(strings.Split(tmp[1], "\n")[0], 64)
			datas[i].X=a
			datas[i].Y=b
		}
	}else if key>=301&&key<=400 {
		c := fmt.Sprintf("%s%05d%s", "./resource/uniform/uniform_", key-300, ".csv")
		f, err := os.Open(c)
		if err != nil {
			fmt.Println(err)
		}
		var a, b float64
		defer f.Close()
		buff := bufio.NewReader(f)
		for i:=0;i<100;i++{
			line, err := buff.ReadString('\n')
			if err == io.EOF {
				break
			}
			tmp := strings.Split(line, ",")
			a, _ = strconv.ParseFloat(tmp[0], 64)
			//string([]byte(tmp[1])[:len(tmp[1]) - 2])
			b, _ = strconv.ParseFloat(strings.Split(tmp[1], "\n")[0], 64)
			datas[i].X=a
			datas[i].Y=b
		}

	}
	//fmt.Println()
	//for _, v := range datass.X {
	//	fmt.Println(v)
	//}
	//for _, v := range datass.Y {
	//	fmt.Println(v)
	//}
	//fmt.Println(datass)
	return datas
}