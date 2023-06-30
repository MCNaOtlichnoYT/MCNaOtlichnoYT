c = require("component")
os.execute("cls")
lp = c.launch_pad
tr = c.transposer
lp.setCoords(0,1)
while true do
  print("Launch pad")
  print("Power:       "..tostring(lp.getEnergyStored()/1000).."%")
  m=tr.getStackInSlot(1,1)
  if m==nil then
    print("Missile:     None")
  else print("Missile:     "..m['label']) end
  x,z=lp.getCoords()
  print("Destination: X="..x.." Z="..z)
  print('============================')
  print('1.Launch')
  print('2.Set X')
  print('3.Set Z')
  print('4.Load missile')
  print('5.Exit')
  c=tonumber(io.read())
  if c==1 then
    lp.launch()
  elseif c==2 then
    x=tonumber(io.read())
    lp.setCoords(x,tonumber(z))
  elseif c==3 then
    z=tonumber(io.read())
    lp.setCoords(tonumber(x),z)
  elseif c==4 then
    ammo={}
    for s=1,54 do
      st=tr.getStackInSlot(0,s)
      if st~=nil then
        tp=st['label']
        if ammo[tp]==nil then
          ammo[tp]=0 end
        ammo[tp]=ammo[tp] + 1
      end
    end
    os.execute("cls")
    print("Available ammo")
    i=1
    atp={}
    for k,v in pairs(ammo) do
      print(tostring(i).."."..k.."("..v..")")
      atp[i]=k
      i=i+1
    end
    n=tonumber(io.read())
    sel_t=atp[n]
    for s=1,54 do
      st=tr.getStackInSlot(0,s)
      if st~=nil then
        if st['label']==sel_t then
          tr.transferItem(0,1,1,s,1)
          break
        end
      end
    end
  elseif c==5 then break
  end
  os.execute("cls")
end