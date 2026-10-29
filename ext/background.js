// Fude: the toolbar button opens the side panel, which paints whatever is playing in the tab beside it
chrome.runtime.onInstalled.addListener(()=>{chrome.sidePanel.setPanelBehavior({openPanelOnActionClick:true}).catch(()=>{})});
chrome.sidePanel.setPanelBehavior({openPanelOnActionClick:true}).catch(()=>{});
