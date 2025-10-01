public class UserDataProcessor {

    private String m_userName;
    private int user_id;
    
    public UserDataProcessor(String name, int id) {
        this.m_userName = name;
        this.user_id = id;
    }
    
    public String GetUserName() {
        return m_userName;
    }
    
    public void P(String sName) {
        System.out.println("Processing user: " + sName);
    }
    
    public static void main(String[] args) {
        String s_name = "Jane Doe";
        int i_d = 12345;
        UserDataProcessor obj = new UserDataProcessor(s_name, i_d);
        obj.P(obj.GetUserName());
    }
}
