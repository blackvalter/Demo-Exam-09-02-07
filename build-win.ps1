param(
 [string]$Python = 'python',
 [string]$Output = (Join-Path $PSScriptRoot 'dist')
)
$ErrorActionPreference = 'Continue'
Push-Location $PSScriptRoot -ErrorAction Stop
try {
 & $Python -m PyInstaller --noconfirm --clean --windowed --distpath $Output ShoeStore.spec
 if ($LASTEXITCODE -ne 0) { throw "PyInstaller failed ($LASTEXITCODE)" }
} finally { Pop-Location }

