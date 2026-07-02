"""The GPS Navigation System (Backtracking)
You're building a GPS app like Google Maps for a hiking trail.
The hiker moves through checkpoints.
If they take a wrong turn, they hit "Go Back" to return to the previous checkpoint.
But once they go back, they can also "Go Forward" if they change their mind again—just like a browser's back/forward buttons.
Operations:
• visit(place) — move to a new place
• back() — go to previous place
• forward() — go forward if available"""
back = []
forward = []
current = "Home"

# Visit
back.append(current)
current = "A"
back.append(current)
current = "B"
back.append(current)
current = "C"

print(current)

# Back
forward.append(current)
current = back.pop()
print(current)

# Back
forward.append(current)
current = back.pop()
print(current)

# Forward
back.append(current)
current = forward.pop()
print(current)