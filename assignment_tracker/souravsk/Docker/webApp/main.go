package main

import (
	"github.com/gofiber/fiber"
)

func hello(c *fiber.Ctx){
	c.Send("Hello Word ")
}

func main(){
	
	app := fiber.New()

	app.Get("/", hello)

	app.Listen(3000)
}