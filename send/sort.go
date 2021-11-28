package send

import (
	"fmt"
	"sort"
)

func sorted(unsort []float64,k int64){
	sort.Float64s(unsort)
	fmt.Println(unsort)
}
