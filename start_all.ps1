# PowerShell script to start both backend and frontend with auto-reload
Write-Host "Starting Chatbot with automatic reload..." -ForegroundColor Green

# Start backend in a new window
Write-Host "Starting Flask backend..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$PWD'; .\start_backend.ps1"

# Wait a moment for backend to start
Start-Sleep -Seconds 3

# Start frontend in a new window
Write-Host "Starting React frontend..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$PWD'; .\start_frontend.ps1"

Write-Host "Both servers started! Check the new windows." -ForegroundColor Green
Write-Host "Backend: http://localhost:5000" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan 