# PowerShell script to start the React frontend automatically
Write-Host "Starting React frontend with auto-reload..." -ForegroundColor Green
Set-Location frontend

# Check if node_modules exists
if (Test-Path "node_modules") {
    Write-Host "Starting React development server..." -ForegroundColor Green
    npm start
} else {
    Write-Host "Installing dependencies first..." -ForegroundColor Yellow
    npm install
    Write-Host "Starting React development server..." -ForegroundColor Green
    npm start
} 