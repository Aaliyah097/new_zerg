# Crypto-platforms connector to serve traffic

# Main Idea
> There are lots of crypto-platforms in the Web and Web3.  
> Generally they all have the same entities and features:
>
> > Accumulate, Manage, Spread Orders;  
> > Accumulate, Manage, Spread Requisites;  
> > Accumulate, Manage, Spread Traders and Clients;  
> 
> The App should be an aggregator of such platforms helping them in traffic serving.  
> Each platform have semi-public API but have a different Data structures of the same Entities.  
> The point is to bring to a single view such entities as orders and requisites managements systems [RMS].
> RMS is a big space for creativity because one platforms use "wallets", others - "requisites" and so on.
>
> **Important notations are:**
> > The App should continuously interact with such platforms, be in consistency state with them;  
> > App's traders should not know anything about these platforms;  
> > No chance for errors...;
> 
> **Idea**  
> Each of such platforms should be represented as an independent component in the App.  
> The App should have one database and one table structures for data of all components.
> 
> **Plan**
> > Bitconce (old Daazweb) [current];  
> > Risex
> 
> **Examples**
> - Bitconce
> > bitconce component has repos folder. This repo has folders: accounts, orders, wallets. They present a facade for bitconce-API.  
> > Each facade process row queries and sends commands to bitconce-api. Row-queries are converted in bitconce-repos-models.  
> > Them are the representation of bitconce data structures without filtering just with adding data types.  
> > So on the App knows bitconce interface.
> > src as the entrance point have such packages as platforms, requisites, users, wallets, etc.  
> >
> > **Each package should have fabrics and mapping mechanisms to each platform component**.  
> > **Each package also knows how does the App want to store data in it's own Database**.
> >
> > So each app also provides an interface. The app's packages should automatically react on domain events on platforms.  
> > It is always a one-sided relationship. Platform's components can not interact with app.
> > 
> > **External data collection services should interact with platform's components and map data and actions to the App.**  
> > **The App should interpret sources via domain entities and send events to platform's components.**
> 
> **Constraints**
> > **The app has to** be very flexible to support many types of currencies: USDT, BTC, etc.  
> > **The app has to** support many types of payment requisites: QIWI, SIM, CARDS, etc.  
> > **The app should not** be strongly coupled, imitate to any of platforms cause their API's and Data structures often being changed.
> 
> **Remember**  
> Platforms's logic, behaviour, data may not meet expectations :)  
> They are all including owners and staff are very different...


# Example
- Getting Orders [flow from component to App]
> Data Collector ➡ bitconce.repo.OrdersRepo ➡ list[BitconceOrder] ➡ src.orders.OrdersRepo ➡ src.orders.Fabric ➡ list[src.orders.Order] ➡ DB
- Add requisite [flow from App to component]
> src.requisites.Requisite ➡ src.requisites.RequisitesRepo ➡ src.requisites.Fabric ➡ BitconceRequisite ➡ bitconce.repos.RequisitesRepo ➡ DB

<hr>

### Alembic
1. go to root folder  
```cd zerg```
2. init alembic folder  
```alembic init alembic```
3. update sqlalchemy.url in alembic.ini file
```dbms_name://user:password@ip_address/db_name```
4. make first migration
```alembic revision --autogenerate -m "init"```
5. migrate
```alembic upgrade head```