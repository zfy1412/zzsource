package send

import (
	"fmt"
	"log"
	"os/exec"
	"strconv"
	"strings"
)

func LcssPrint(Keylength int,datasetnum int,thresholddataset int)(float64,float64){

	KeyLength:=strconv.Itoa(Keylength)

	thresholdDataset:=strconv.Itoa(thresholddataset)
	var chosen2 string
	if datasetnum>=1&&datasetnum<=100{
		chosen2 ="normal"

	}else if datasetnum>=101&&datasetnum<=200{
		chosen2 ="SHH-Taxi"
		datasetnum=datasetnum-100
	}else if datasetnum>=201&&datasetnum<=300{
		chosen2 ="T-drive"
		datasetnum=datasetnum-200
	}else if datasetnum>=301&&datasetnum<=400{
		chosen2 ="uniform"
		datasetnum=datasetnum-300
	}
	datasetNum:=strconv.Itoa(datasetnum)
	cmd:=exec.Command("python","main.py",KeyLength, datasetNum, chosen2, thresholdDataset)
	cmd.Dir="D:\\code\\mapweb\\algorithm\\lcss"
	output,err:=cmd.Output()
	if err!=nil{
		log.Fatalln(err)
	}
	tmp := strings.Split(string(output), "\r\n")
	a,_:=strconv.ParseFloat(tmp[0],64)
	b,_:=strconv.ParseFloat(tmp[1],64)
	fmt.Println(a)
	fmt.Println(b)
	return a,b
}

func DTWPrint(Keylength int,datasetnum int)(float64,float64){
	var chosen2 string
	if datasetnum>=1&&datasetnum<=100{
		chosen2 ="normal"

	}else if datasetnum>=101&&datasetnum<=200{
		chosen2 ="SHH-Taxi"
		datasetnum=datasetnum-100
	}else if datasetnum>=201&&datasetnum<=300{
		chosen2 ="T-drive"
		datasetnum=datasetnum-200
	}else if datasetnum>=301&&datasetnum<=400{
		chosen2 ="uniform"
		datasetnum=datasetnum-300
	}
	KeyLength:=strconv.Itoa(Keylength)
	datasetNum:=strconv.Itoa(datasetnum)
	cmd:=exec.Command("python","main.py",KeyLength, datasetNum, chosen2)
	cmd.Dir="D:\\code\\mapweb\\algorithm\\DTW"
	output,err:=cmd.Output()
	if err!=nil{
		log.Fatalln(err)
	}
	tmp := strings.Split(string(output), "\r\n")
	a,_:=strconv.ParseFloat(tmp[0],64)
	b,_:=strconv.ParseFloat(tmp[1],64)
	fmt.Println(a)
	fmt.Println(b)
	return a,b
}

func SecurePrint(Keylength int,datasetnum int,thresholddataset int)(float64,float64){

	KeyLength:=strconv.Itoa(Keylength)
	datasetNum:=strconv.Itoa(datasetnum)
	thresholdDataset:=strconv.Itoa(thresholddataset)
	var chosen2 string
	if datasetnum>=1&&datasetnum<=100{
		chosen2 ="normal"
	}else if datasetnum>=101&&datasetnum<=200{
		chosen2 ="SHH-Taxi"
		datasetnum=datasetnum-100
	}else if datasetnum>=201&&datasetnum<=300{
		chosen2 ="T-drive"
		datasetnum=datasetnum-200
	}else if datasetnum>=301&&datasetnum<=400{
		chosen2 ="uniform"
		datasetnum=datasetnum-300
	}
	cmd:=exec.Command("python","main.py",KeyLength,thresholdDataset,chosen2,  datasetNum)
	cmd.Dir="D:\\code\\mapweb\\algorithm\\Secure-Trajectory-Similarity-Computation"
	output,err:=cmd.Output()
	if err!=nil{
		log.Fatalln(err)
	}
	tmp := strings.Split(string(output), "\r\n")
	a,_:=strconv.ParseFloat(tmp[0],64)
	b,_:=strconv.ParseFloat(tmp[1],64)
	fmt.Println(a)
	fmt.Println(b)
	return a,b
}
