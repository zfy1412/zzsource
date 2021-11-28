package send


type Datatry struct{
	X float64 `json:"longitude"`
	Y float64 `json:"latitude"`
}
var datatry[] Datatry=make([]Datatry,0,1000)

func Try() []Datatry{

	var point Datatry
	point.X=40.99853
	point.Y=123.00008
	datatry=append(datatry,point)
	point.X=46.614926
	point.Y=-122.1941151
	datatry=append(datatry,point)
	point.X=45.61495
	point.Y=-122.194111
	datatry=append(datatry,point)
	point.X=43.61495
	point.Y=-122.194111
	datatry=append(datatry,point)
	point.X=41.61495
	point.Y=-122.194111
	datatry=append(datatry,point)
	point.X=40.614925
	point.Y=-122.194115
	datatry=append(datatry,point)
	point.X=42.614926
	point.Y=-122.1941151
	datatry=append(datatry,point)
	point.X=44.61495
	point.Y=-122.194111
	datatry=append(datatry,point)
	point.X=39.61495
	point.Y=-122.194111
	datatry=append(datatry,point)
	point.X=33.61495
	point.Y=-122.194111
	datatry=append(datatry,point)



	point.X=47.614925
	point.Y=-126.194115
	datatry=append(datatry,point)
	point.X=46.614926
	point.Y=-126.1941151
	datatry=append(datatry,point)
	point.X=45.61495
	point.Y=-126.194111
	datatry=append(datatry,point)
	point.X=43.61495
	point.Y=-126.194111
	datatry=append(datatry,point)
	point.X=41.61495
	point.Y=-126.194111
	datatry=append(datatry,point)
	point.X=40.614925
	point.Y=-126.194115
	datatry=append(datatry,point)
	point.X=42.614926
	point.Y=-126.1941151
	datatry=append(datatry,point)
	point.X=44.61495
	point.Y=-126.194111
	datatry=append(datatry,point)
	point.X=39.61495
	point.Y=-126.194111
	datatry=append(datatry,point)
	point.X=33.61495
	point.Y=-126.194111
	datatry=append(datatry,point)

	return datatry
}
