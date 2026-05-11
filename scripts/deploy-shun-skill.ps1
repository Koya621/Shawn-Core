$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$source = Join-Path $repoRoot "Shawn-Core-upload\codex-skill\Shawn"
$workspaceTarget = "D:\Think Codex\Design Team\skills\shun-designer"
$globalTarget = Join-Path $env:USERPROFILE ".codex\skills\shun-designer"

if (-not (Test-Path $source)) {
  throw "Source skill not found: $source"
}

function Sync-Folder {
  param(
    [Parameter(Mandatory = $true)][string]$From,
    [Parameter(Mandatory = $true)][string]$To
  )

  New-Item -ItemType Directory -Force -Path $To | Out-Null
  Get-ChildItem -Path $To -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
  Copy-Item -Path (Join-Path $From "*") -Destination $To -Recurse -Force
}

Sync-Folder -From $source -To $workspaceTarget
Sync-Folder -From $source -To $globalTarget

Write-Output "OK: deployed shun-designer skill"
Write-Output "SOURCE: $source"
Write-Output "WORKSPACE_TARGET: $workspaceTarget"
Write-Output "GLOBAL_TARGET: $globalTarget"
