-- Simple Roblox game script example
-- Creates a clickable part that changes color when clicked.

local workspace = game:GetService("Workspace")

local part = Instance.new("Part")
part.Name = "ClickPart"
part.Size = Vector3.new(4, 1, 4)
part.Position = Vector3.new(0, 5, 0)
part.Anchored = true
part.BrickColor = BrickColor.new("Bright red")
part.Parent = workspace

local clickDetector = Instance.new("ClickDetector")
clickDetector.Parent = part

local colors = {
    BrickColor.new("Bright red"),
    BrickColor.new("Bright blue"),
    BrickColor.new("Bright green"),
    BrickColor.new("Bright yellow")
}

local currentColorIndex = 1

clickDetector.MouseClick:Connect(function(player)
    currentColorIndex = currentColorIndex % #colors + 1
    part.BrickColor = colors[currentColorIndex]
    print(player.Name .. " clicked the part!")
end)

local spawnLocation = Instance.new("SpawnLocation")
spawnLocation.Name = "Spawn"
spawnLocation.Size = Vector3.new(6, 1, 6)
spawnLocation.Position = Vector3.new(0, 1, 0)
spawnLocation.Anchored = true
spawnLocation.Neutral = true
spawnLocation.Parent = workspace
