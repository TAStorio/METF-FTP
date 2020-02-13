commands.add_command("fooping", "", function(table)
	rcon.print("pong")
	game.print("ping was called")
end)

