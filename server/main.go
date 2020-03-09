package main

import (
	"context"
	"fmt"
	"net"

	calculations "github.com/krnblni/GoPythonGRPC/proto/go"
	"google.golang.org/grpc"
)

type calculationsServer struct{}

func (cs *calculationsServer) Add(ctx context.Context, inputs *calculations.NumAB) (*calculations.ResAB, error) {
	a, b := inputs.GetA(), inputs.GetB()
	return &calculations.ResAB{Ans: a + b}, nil
}

func (cs *calculationsServer) Subtract(ctx context.Context, inputs *calculations.NumAB) (*calculations.ResAB, error) {
	a, b := inputs.GetA(), inputs.GetB()
	return &calculations.ResAB{Ans: a - b}, nil
}

func (cs *calculationsServer) Multiply(ctx context.Context, inputs *calculations.NumAB) (*calculations.ResAB, error) {
	a, b := inputs.GetA(), inputs.GetB()
	return &calculations.ResAB{Ans: a * b}, nil
}

func (cs *calculationsServer) Divide(ctx context.Context, inputs *calculations.NumAB) (*calculations.ResAB, error) {
	a, b := inputs.GetA(), inputs.GetB()
	return &calculations.ResAB{Ans: a / b}, nil
}

func main() {
	listener, err := net.Listen("tcp", ":3080")
	if err != nil {
		fmt.Println("Unable to create a listener... ", err)
		return
	}

	server := grpc.NewServer()

	calculations.RegisterCalculateServer(server, &calculationsServer{})

	if err := server.Serve(listener); err != nil {
		fmt.Println("Could not create a server...", err)
		return
	}
}
