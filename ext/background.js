// Fude: the toolbar button (or Alt+Shift+F) opens the side panel beside the tab and lets Fude hear that tab.
// Chrome only lets an extension hear a tab after its button was pressed on that tab, so the press is handled here:
// it opens the panel, asks Chrome for the tab's sound at once, and tells the panel which tab to paint
chrome.runtime.onInstalled.addListener(()=>{chrome.sidePanel.setPanelBehavior({openPanelOnActionClick:false}).catch(()=>{})});
chrome.sidePanel.setPanelBehavior({openPanelOnActionClick:false}).catch(()=>{});
chrome.action.onClicked.addListener(tab=>{
  chrome.sidePanel.open({windowId:tab.windowId}).catch(()=>{});
  const tell=streamId=>{const v={tabId:tab.id,streamId:streamId||'',at:Date.now()};chrome.storage.session.set({fudeTab:v}).catch(()=>{});chrome.runtime.sendMessage({fude:'tab',...v}).catch(()=>{})};
  if(!/^https?:/.test(tab.url||'https:'))return tell('');
  chrome.tabCapture.getMediaStreamId({targetTabId:tab.id},id=>{void chrome.runtime.lastError;tell(id)});
});
