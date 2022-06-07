package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
	"time"

	"github.com/golang/geo/r3"
	quickhull "github.com/markus-wa/quickhull-go/v2"
)

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
func main() {
	pointCloud, err := loadPoints("data/data2D.txt")
	start := time.Now()
	checkError(err)
	hull := new(quickhull.QuickHull).ConvexHull(pointCloud, true, false, 0)
	center := r3.Vector{X: 0, Y: 0, Z: 0}
	for _, point := range hull.Vertices {
		center = center.Add(point)
	}
	center = center.Mul(1.0 / float64(len(hull.Vertices)))
	// for each triangle in the hull find the angle between the edges, and keep track of the point with the smallest angle
	BestPoint := r3.Vector{X: 0, Y: 0, Z: 0}
	BestAngle := 100.0
	bestIndex := 0
	for i, v := range hull.Vertices {
		thisVsMaxAngle := 0.0
		for j, v2 := range hull.Vertices {
			if i == j {
				continue
			}
			angle := findAngle(v, center, v2)
			if angle > thisVsMaxAngle {
				thisVsMaxAngle = angle
			}
		}
		if thisVsMaxAngle < BestAngle {
			BestAngle = thisVsMaxAngle
			BestPoint = v
			bestIndex = i
		}
	}
	println("index of best Point = " + strconv.Itoa(bestIndex))
	println("BestPoint = " + BestPoint.String())
	println("BestAngle = " + strconv.FormatFloat(BestAngle, 'f', 2, 64))
	fmt.Println("this took " + time.Since(start).String())
	fmt.Println(BestPoint)
}
func findAngle(p1, p2, p3 r3.Vector) float64 {
	ba := p1.Sub(p2)
	bc := p1.Sub(p3)
	cosine_angle := ba.Dot(bc) / (ba.Norm() * bc.Norm())
	return math.Acos(cosine_angle)
}
func loadPoints(filename string) (pointCloud []r3.Vector, err error) {
	data, err := ioutil.ReadFile(filename)
	checkError(err)
	pointCloud = []r3.Vector{}
	for _, line := range strings.Split(string(data), "\n") {
		if line != "" {
			parts := strings.Split(line, " ")
			if len(parts) != 2 {
				continue
			}
			x, err := strconv.ParseFloat(parts[0], 64)
			if err != nil {
				continue
			}
			y, err := strconv.ParseFloat(parts[1], 64)
			if err != nil {
				continue
			}
			pointCloud = append(pointCloud, r3.Vector{X: x, Y: y, Z: 1})
		}
	}
	print("loaded " + strconv.Itoa(len(pointCloud)) + " points")
	return
}
