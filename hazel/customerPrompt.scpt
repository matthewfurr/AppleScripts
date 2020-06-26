tell application "Finder" to set shortName to name of (theFile as alias)

set theDialogText to "Customer Name:"
set theButtonIfPressedTheRuleWillContinue to "OK"
set theButtonIfPressedRuleAborts to "Skip"
set theDialogTitle to "Advanced Hazel Renaming"

tell application "System Events"
	activate
	set theResult to (display dialog theDialogText with title theDialogTitle default answer "" buttons {theButtonIfPressedTheRuleWillContinue, theButtonIfPressedRuleAborts} default button 1 giving up after 60 with icon (POSIX file (POSIX path of (get path to library folder from user domain) & "/PreferencePanes/Hazel.prefPane/Contents/Resources/Hazel.icns" as string) as string) as alias)
end tell

if (button returned of theResult) is theButtonIfPressedTheRuleWillContinue then
	set theText to text returned of theResult
	return {hazelExportTokens:{CustomerCode:theText}}
end if

return {hazelExportTokens:{CustomerCode:shortName}}
