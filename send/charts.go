package send

type Test struct{
	T1 []float64  `json:"Lcssdata"`
	T2 []float64  `json:"DTWdata"`
	T3 []float64  `json:"Securedata"`
	L []string `json:"legend"`
}
var te Test
func Runtime(chosen [30]string,num int,ketlengthtime1[100] float64,ketlengthtime2[100] float64,ketlengthtime3[100] float64)Test{


	for i := 0; i < num; i++ {
		te.T1=append(te.T1,ketlengthtime1[i])
	}
	for i := 0; i < num; i++ {
		te.T2=append(te.T2,ketlengthtime2[i])
	}
	for i := 0; i < num; i++ {
		te.T3=append(te.T3,ketlengthtime3[i])
	}


	for i := 0; i < num; i++ {
		if(chosen[i]=="LCSS"){
			te.L=append(te.L,"SLCSS")
		}else if(chosen[i]=="DTW"){
			te.L=append(te.L,"SDTW")
		}else{
			te.L=append(te.L,"SBD")
		}
	}
	return te
}


var average Test
func Average(chosen [30]string,num int,ketlengthtime1[100] float64,ketlengthtime2[100] float64,ketlengthtime3[100] float64)Test {



	for i := 0; i < num; i++ {
		average.T1=append(average.T1,ketlengthtime1[i])
	}
	for i := 0; i < num; i++ {
		average.T2=append(average.T2,ketlengthtime2[i])
	}
	for i := 0; i < num; i++ {
		average.T3=append(average.T3,ketlengthtime3[i])
	}
	for i := 0; i < num; i++ {
		if(chosen[i]=="LCSS"){
			average.L=append(average.L,"SLCSS")
		}else if(chosen[i]=="DTW"){
			average.L=append(average.L,"SDTW")
		}else{
			average.L=append(average.L,"SBD")
		}
	}
	return average
}

var me Test
func Mermory(chosen [30]string,num int,ketlengthtime1[100] float64,ketlengthtime2[100] float64,ketlengthtime3[100] float64)Test{



	for i := 0; i < num; i++ {
		me.T1=append(me.T1,ketlengthtime1[i])
	}
	for i := 0; i < num; i++ {
		me.T2=append(me.T2,ketlengthtime2[i])
	}
	for i := 0; i < num; i++ {
		me.T3=append(me.T3,ketlengthtime3[i])
	}

	for i := 0; i < num; i++ {
		if(chosen[i]=="LCSS"){
			me.L=append(me.L,"SLCSS")
		}else if(chosen[i]=="DTW"){
			me.L=append(me.L,"SDTW")
		}else{
			me.L=append(me.L,"SBD")
		}
	}
	return me
}